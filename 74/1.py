# Method Overriding

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x + self.y


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area(self):
        return 3.14 * super().area()


# Creating an instance of the Shape class
rec = Shape(3, 5)
print("Area of Shape:", rec.area())

# Creating an instance of the Circle class
c = Circle(5)
print("Area of Circle:", c.area())
