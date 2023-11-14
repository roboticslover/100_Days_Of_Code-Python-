text = input("Enter your message---")

# Encoding
print("Encoding---")
if len(text) <= 3:
    encode = text[1:]+text[:1]
    print(encode)
else:
    encode = text[::-1]
    print(encode)

# Decoding
print("Decoding---")
if len(encode) <= 3:
    decode = encode[-1]+encode[:-1]
    print(decode)
else:
    decode = encode[::-1]
    print(decode)
