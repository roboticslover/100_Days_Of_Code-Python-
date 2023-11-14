class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):
        # protected method
        return "CodeWithHarry"


obj = Student()

obj = Student()
print(obj._name)
print(obj._funName())
