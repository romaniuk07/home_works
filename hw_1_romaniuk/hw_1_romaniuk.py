import math

# Завдання 1:

# 1)
name = 'Oleksandr'

surname = 'Romaniuk'

print(name + ' ' + surname)

# 2)

print(name.lower() + ' ' + surname.lower())
print(name.capitalize() + ' ' + surname.capitalize())

# 3)
name_with_spaces = '\t' + name + '\t'

surname_with_spaces = '\t' + surname + '\t'

print(name_with_spaces + '\n' + surname_with_spaces)

print(name_with_spaces.strip() + ' ' + surname_with_spaces.strip())

# Завдання 2:

radius = 20

# довжина кола
circumference = 2 * math.pi * radius
# площа кола
area = math.pi * radius ** 2

print('Довжина кола:' + str(circumference))
print('Площа кола:' + str(area))

# Завдання 3:

# 1)
dollar_rate = 39.0000

# 2)
conversion_in_uah = dollar_rate * 1000.00

# 3)
print(round(conversion_in_uah, 2))
print('Поточний курс складає:' + ' ' + str(dollar_rate))

