from datetime import datetime, date ,time

from db import people
from application import salary

if __name__ == "__main__":
    t = datetime.now().strftime('%d-%m-%Y %H:%M')

    print(f"Время {t}")
    earn = salary.calculate_salary()
    people.get_employees(earn)
