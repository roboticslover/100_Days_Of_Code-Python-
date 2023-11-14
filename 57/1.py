# Classes and Objects

class Person:
    name = "Harry"
    occupation = "Software Developer"

    def info(self):
        print(f"{self.name} is a {self.occupation}.")


a = Person()
a.occupation = "Data Scientist"
a.info()
