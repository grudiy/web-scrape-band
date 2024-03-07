import time
import requests
import selectorlib
import os
import sqlite3

URL = "http://programmer100.pythonanywhere.com/tours"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


class Event:
    def scrape(self, url):
        """Scrape the page source from the URL"""
        response = requests.get(url, headers=HEADERS)
        source = response.text
        return source

    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return value


class Email:
    def send(self, msg):
        # Just a mock of email sending function
        print(msg)
        print("Email was sent!")


class Database:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
    def store(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO events VALUES(?, ?, ?)", row)
        self.connection.commit()

    def read(self, extracted):
        row_arg = extracted.split(",")
        row_arg = [item.strip() for item in row_arg]
        band, city, date = row_arg
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
        rows = cursor.fetchall()
        print(rows)
        return rows

if __name__ == "__main__":
    while True:
        event = Event()
        scraped = event.scrape(URL)
        extracted = event.extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            database = Database(db_path="data.db")
            row = database.read(extracted)
            if not row:
                database.store(extracted)
                email = Email()
                email.send("New events found!")
        time.sleep(2)

