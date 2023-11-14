# Generators in Python

def my_generator():
    for i in range(1, 7):
        yield i


gen = my_generator()
print(next(gen))
