# Access Modifiers
# Python don't have concept of ---Public,Private,Protected

class Employee:
    # Private Access Specifier
    def __init__(self):
        self.__name = "Harry"


a = Employee()

# Cannot be accessed directly
# print(a.__name)

# can be accessed indirectly
print(a._Employee__name)
