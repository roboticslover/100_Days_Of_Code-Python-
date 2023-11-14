# Lambda

def appl(fx, value):
    return 7 + fx(*value)


avg = lambda *args: sum(args) / len(args)
print("avg:", avg(7, 8, 6))

result = appl(avg, (7, 8, 6))
print("Result:", result)
