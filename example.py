import sqlite3

# Establish connection to DB
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query data
cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

# Insert new rows
new_rows = [('Cats', 'Cats City', '2088.10.17'),
            ('Hens', 'Hens City', '2088.10.17')]

cursor.executemany("INSERT INTO events VALUES(?, ?, ?)", new_rows)
connection.commit()

# Query all data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)