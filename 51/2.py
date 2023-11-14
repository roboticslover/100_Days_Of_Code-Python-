with open('51/file2.txt', 'w') as f:
    f.write('Hello World!!!')
    f.truncate(5)

with open('51/file2.txt', 'r') as f:
    print(f.read())
