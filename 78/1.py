# Single Inheritance

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!")


d = Dog(name="Buddy", breed="Labrador")
d.make_sound()

a = Animal(name="Generic Animal", species="Unknown")
a.make_sound()
