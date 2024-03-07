class User:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        name = self.name.upper()
        return name

    def age(self, current_year):
        age = current_year - self.birthyear
        return age


john = User("John", 1999)

print(john.age(2023))
print(john.get_name())