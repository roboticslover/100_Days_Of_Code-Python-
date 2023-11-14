import pyttsx3

names = ["Rahul", "Nishant", "Harry"]

engine = pyttsx3.init()

for person in names:
    shoutout = f"Shout-out to {person}"

    engine.say(shoutout)

    engine.runAndWait()
