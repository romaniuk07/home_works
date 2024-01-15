import random
import math


# Задача 1

min = random.randint(0, 59)

if min <= 15 :
    print(min, "в першій половині")
elif min >= 16 and min <= 30 :
    print(min, "друга половина")
elif min >= 31 and min <= 45 :
    print(min, "третя половина")
else :
    print(min, "четверта половина")

# Задача 2

birth_month = input("Enter your birth month number: ")

if birth_month.isdigit() :
    birth_month = int(birth_month)

    if birth_month == 12 or birth_month >= 1 and birth_month <= 2 :
     birth_month = "Зима - За вікном падав сніг."
    elif birth_month >= 3 and birth_month <= 5 :
      birth_month = "Весна - Все довкола розцвітало."
    elif birth_month >= 6 and birth_month <= 8 :
      birth_month = "Літо - Діти насолоджувались літніми канікулами."
    elif birth_month >= 9 and birth_month <= 11 :
      birth_month = "Осінь - Все довкола загоралось яскравими фарбами."
    else:
        print("Range of birth months 1 - 12")
else:
    print("You entered an invalid data")

print(birth_month)

# Задача 3

random_number = int(random.randint(10, 10000))
print(f"рандомне число {random_number}")

last_digit = random_number % 10
print(f"{last_digit} остання цифра рандомного числа")

if last_digit % 2 == 0:
    print(f'остання цифра {last_digit} парна')
    total = 0
    for digit in str(random_number):
        total += int(digit)
    print(f'сума чисел рандомного числа {total}')
    if total % 3 == 0:
        print(f"Число {total} ділиться на 6")
    else:
        print(f"Число {total} не ділиться на 6")
else:
    print(f"стання цифра рандомного числа {last_digit} не парна")

# Задача 4

x_input = input("Введіть координату x: ")
y_input = input("Введіть координату y: ")

if '.' in x_input:
    x_parts = x_input.split('.')
    if len(x_parts) == 2 and x_parts[0].lstrip('-').isdigit() and x_parts[1].isdigit():
        x = float(x_input)
elif x_input.lstrip('-').isdigit():
    x = int(x_input)
else:
    print("Невірне значення для x.")

if '.' in y_input:
    y_parts = y_input.split('.')
    if len(y_parts) == 2 and y_parts[0].lstrip('-').isdigit() and y_parts[1].isdigit():
        y = float(y_input)
elif y_input.lstrip('-').isdigit():
    y = int(y_input)
else:
    print("Невірне значення для y.")

if x > 0 and y > 0:
    print("Перша координатна чверть")
elif x < 0 and y > 0:
    print("Друга координатна чверть")
elif x < 0 and y < 0:
    print("Третя координатна чверть")
elif x > 0 and y < 0:
    print("Четверта координатна чверть")
elif x == 0 and y == 0:
    print("Точка є початком осі координат")
elif x == 0:
    print('Точка на осі y')
elif y == 0:
    print('Точка на осі x')
else:
    print("Невірне значення")
