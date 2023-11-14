# Inheritance

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee-{self.id} is {self.name}.")


class Programmer(Employee):
    def showLanguage(self):
        print("The default language is python.")


e = Programmer("Sachin", 7)
e.showDetails()
e.showLanguage()
