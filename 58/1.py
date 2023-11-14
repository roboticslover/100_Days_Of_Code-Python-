# Constructors

class Person:
    def __init__(self, name, occ):
        print("This is a constructor!!!")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("Sachin", "Data Scientist.")
a.info()
