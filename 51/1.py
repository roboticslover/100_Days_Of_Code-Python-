with open('51/file.txt', 'r') as f:
    print(type(f))

    # Move to the 10th Byte in the file
    f.seek(10)

    # Read the next 5 bytes
    print(f.tell())
    data = f.read(5)
    print(data)
