# Function Caching

from functools import lru_cache
import time


@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5


print(fx(20))
print("done for 20")
print(fx(21))
print("done for 21")
print(fx(22))
print("done for 22")

print(fx(20))
print("done for 20")
print(fx(21))
print("done for 21")
print(fx(22))
print("done for 22")
