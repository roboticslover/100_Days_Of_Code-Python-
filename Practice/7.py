import os

files = os.listdir('example')

i = 1
for file in files:
    if file.endswith(".py"):
        os.rename(f"example/{file}", f"example/{i}.py")
        i = i+1
