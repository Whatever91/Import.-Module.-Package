from datetime import datetime

import cowsay
import pyttsx3

from application.salary import calculate_salary
from application.db.people import get_employees


def cow_say():
    engine = pyttsx3.init()
    phrase = "Python is my favorite programming language"
    cowsay.cow(phrase)
    engine.say(phrase)
    engine.runAndWait()


if __name__ == '__main__':
    print("Не сегодня:", datetime.now().strftime("%H:%M:%S %d-%m-%Y "))
    get_employees()
    calculate_salary()
    cow_say()