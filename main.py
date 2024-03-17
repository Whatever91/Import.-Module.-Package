from datetime import datetime
import configparser

from Application.DataBase.people import get_employees
from Application.salary import calculate_salary


def now_utcnow():
    print('Знакомство с модулем "datetime".\nЗапуск функции:')
    print(f'Текущая дата и время: {datetime.now()}')
    print(f'Текущая дата и время UTC: {datetime.utcnow()}\n')


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    now_utcnow()
