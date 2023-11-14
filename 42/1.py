# Enumerate Functions

marks = [12, 56, 32, 98, 12, 45, 1, 4]

for index, mark in enumerate(marks, start=1):
    print(mark)
    if (index == 3):
        print("Here , I don't need to declare index as a variable and increment that!!!")
