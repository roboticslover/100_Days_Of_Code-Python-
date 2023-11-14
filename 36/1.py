try:
    num = int(input("Enter an Integer: "))
    a = [6, 7]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error.")
