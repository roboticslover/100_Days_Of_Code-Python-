x = 7

match x:
    case 0:
        print("zero")
    case 4:
        print("four")
    case _ if x != 90:
        print(x, "is not 90")
    case _:
        print("not valid!!!")
