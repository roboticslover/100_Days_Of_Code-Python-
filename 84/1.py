# Time Module

# time.time()
import time


def UsingFor():
    for i in range(7):
        print(i)


init = time.time()
UsingFor()
t1 = time.time()-init
print(t1)

# time.sleep()
print(69)
time.sleep(3)
print("This is printed after 3 seconds!!!")

# strftime
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d,%H:%M:%S", t)
print(formatted_time)
