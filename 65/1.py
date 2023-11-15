# Static Method
# Static Method: In Python, a static method is a method that belongs to a class rather than an instance of the class.
# They can be called on the class itself, without creating an instance.

class Math:
    def __init__(self, num):
        self.num = num

    @staticmethod
    def add(a, b):
        return a+b


a = Math(5)
print(a.num)

print(Math.add(5, 2))
