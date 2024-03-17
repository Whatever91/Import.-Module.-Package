from datetime import datetime

def get_employees():
    print('Запускаем функцию get_employees() из модуля people.py')
    print(f'Дата и время: {datetime.now()}')
    print(f'Дата и время UTC: {datetime.utcnow()}\n')