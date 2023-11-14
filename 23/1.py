l = [11, 45, 1, 2, 4, 6, 1, 1]

# append
l.append(7)
print(l)

# Sort
l.sort
print(l)
l.sort(reverse=True)
print(l)

# reverse
l.reverse()
print(l)

# index
print(l.index(1))

# count
print(l.count(1))

# copy
m = l.copy()
print(m)

# insert
l.insert(0, 69)
print(l)

# extend
m = ['a', 'b', 'c']
l.extend(m)
print(l)
