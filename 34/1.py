ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

# update
ep1.update(ep2)
print(ep1)

# pop
ep1.pop(122)
print(ep1)
ep1.popitem()
print(ep1)

# clear
ep2.clear()
print(ep2)

# del
del ep1[123]
print(ep1)
del ep2
print(ep2)
