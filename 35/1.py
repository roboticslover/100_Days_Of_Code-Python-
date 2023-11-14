# else loop with for and while
for i in []:
    print(i)
else:
    print("sorry loop completed!!!")

# else loop won't work when loop breaks
for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("else don't get applied!!!")
