import pyttsx3
import time
from plyer import notification


def notify(reminder_text):
    notification.notify(
        title='Drink Water Reminder',
        message=reminder_text,
        timeout=10
    )


engine = pyttsx3.init()
reminder = "Drink Water"

while True:
    engine.say(reminder)
    engine.runAndWait()
    notify(reminder)
    time.sleep(3)
