import time as t

time = int(t.strftime('%H'))

if time >= 6 and time <= 12:
    print("Good Morning.")
elif time >= 12 and time <= 18:
    print("Good Afternoon.")
else:
    print("Good Evening.")
