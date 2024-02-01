from functools import reduce

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
     21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
b = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 7, 8, 9, 10, 11, 12, 13, 14]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Задача 1: Напишіть програму на Python для знаходження перетину двох
# заданих масивів за допомогою лямбда.

intersect = lambda a, b: list(set(a).intersection(set(b)))

print(f'Перетин між двома списками a i b є {intersect(a, b)}')



# Задача 2: Напишіть програму на Python, щоб перевірити, чи є
# заданий рядок числом, за допомогою лямбда

# Для перевірки створив 2 перемінні різних типів данних
stringa = 'hello'
number = 0

verify_str_type = lambda value: f'є типом str' if type(value) is str \
    else f'не є типом str'

# Перевірка чи правильно працює функція
print(verify_str_type(stringa))
print(verify_str_type(number))



# Задача 3: Напишіть програму на Python, щоб знайти список із максимальною та
# мінімальною довжиною за допомогою лямбда.

# Моя логіка в вирішенні задачі
# Створити пермінну словник яка буде приймати ключ - назву перемінної списку,
# а значення - вміст.Це для того,щоб вивести назву списку

lists_dict = dict()

# Перемінна наповнюється через цикл(для оновлення данних,якщо в список додадуть
# нові значення)
def create_dict_from_list():
    for _ in a:
        lists_dict['a'] = lists_dict.get('key', []) + a
    for _ in b:
        lists_dict['b'] = lists_dict.get('key', []) + b
    for _ in c:
        lists_dict['c'] = lists_dict.get('key', []) + c
    return lists_dict

create_dict_from_list()

# Далі для знаходження мin і max довжини списку я створюю функції в яких
# є перемінні котрі в свою чергу міститять лямбда функцію

#   max_key  перемінна визначає ключ з словника який має найбільше значення.
#   Аналогічно in_key

def max_len():
    max_key = max(lists_dict, key=lambda list_name: len(lists_dict[list_name]))
    max_value = lists_dict[max_key]

    return print(f'Найдовший список це \'{max_key}\', його довжина {len(max_value)}')


def min_len():
    min_key = min(lists_dict, key=lambda list_name: len(lists_dict[list_name]))
    min_value = lists_dict[min_key]

    return print(f'Найкоротший список це \'{min_key}\' його довжина {len(min_value)}')

# Відтворення функцій (які прінтують визначені максимальні і мінімальні
# списки за довжиною)
min_len()
max_len()
