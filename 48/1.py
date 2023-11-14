# global_keyword

x = 10


def my_function():
    global x
    x = 69
    y = 5


my_function()
print(x)
print(y)
