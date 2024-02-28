from datetime import datetime, timedelta
import requests

# Реалізуйте функцію, яка додає або віднімає від заданої дати певну кількість днів. Приймає на вхід будь-яку дату
# та час (datetime), а також значення днів(int), і знак(True або False, які репрезентують + і -). Повертає datetime.
# В цій задачі скористайтесь datetime.timedelta

def add_or_subtract_days(datetime, days, is_subtraction=False):
    sign = -1 if is_subtraction else 1

    result_datetime = datetime + sign * timedelta(days=days)

    return result_datetime


current_datetime = datetime.now()
result_after_addition = add_or_subtract_days(current_datetime, 5)
result_after_subtraction = add_or_subtract_days(current_datetime, 3, is_subtraction=False)

print("Поточна дата і час:", current_datetime)
print("Після додавання 5 днів:", result_after_addition)
print("Після віднімання 3 днів:", result_after_subtraction,'\n')


# Реалізуйте функцію, яка вираховує ваш точний вік(не обов('язково вказувати свої данні), вираховуючі різницю між '
# 'наданим значенням і значенням datetime.now(). Приймає дату та час(datetime), повертає три значення: datetime.timedelta, '
# 'datetime.timestamp прожитого життя і строкове значення часу народження в форматі (рік(останні два числа, день, місяць, '
# 'години, хвилини,секунди, am/pm в 12 годинному форматі). Виведіть результат в консоль)


def calculate_age(birth_datetime):
    current_datetime = datetime.now()
    age_timedelta = current_datetime - birth_datetime
    age_timestamp = age_timedelta.total_seconds()

    birth_date_str = birth_datetime.strftime("%y-%d-%m %I:%M:%S %p")

    return age_timedelta, age_timestamp, birth_date_str

year_birth = input('Ведіть рік свого народження:')
month_birth = input('Ведіть місяць свого народження(без 0):')
day_birth = input('Ведіть день свого народження:')
hour_birth = input('Ведіть годину свого народження:')
minute_birth = input('Ведіть хвилини свого народження:')
second_birth = input('Ведіть годину секунди народження:')

birth_datetime = datetime(int(year_birth), int(month_birth), int(day_birth), 12, 0, 0)
age_timedelta, age_timestamp, birth_date_str = calculate_age(birth_datetime)

print('\n' "Прожите час: ", age_timedelta)
print("Прожите час у секундах: ", age_timestamp)
print("Дата народження: ", birth_date_str,'\n')


# Створіть обробку одного будь-якого exception, який не використався як приклад на занятті, додайте обробку
# решти ексепшенів за допомогою Exception. Виведіть результат в консоль

def req(address):
    try:
        response = requests.get(address)
        response.raise_for_status()
    except requests.exceptions.HTTPError as he:
        print(f"HTTP Error: {he}")
    except requests.exceptions.RequestException as re:
        print(f"Request Exception: {re}")


req(r"hps://example.com")