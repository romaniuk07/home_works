import random

# Задача:1

first_list = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
second_list = [4, 9, 6, 11, 8, 5, 10, 7]


def find_similar_items():
    similar_items = list(set(first_list) & set(second_list))
    print(similar_items)


find_similar_items()

# Задача:2

students = {'Vasyl': 7, 'Petro': 4, 'Anton': 9, 'Stepan': 12, 'Orest': 10,
            'Maksym': 2}


def average_grade(students):
    numbers_value = list(students.values())
    average = sum(numbers_value) / len(numbers_value)

    keys_above_average = {key: value for key, value in students.items() if
                          value >= average}
    print(f'Середній бал: {round(average, 1)}')
    print(f"Cтуденти з балами вище середнього {keys_above_average}:", )


average_grade(students)

# Задача:3

name_list = ['Анатолій', 'Василь', 'Галина', 'Дмитро', 'Євгенія', 'Жанна',
             'Зіновій', 'Ірина', 'Костянтин',
             'Людмила', 'Микола', 'Наталія', 'Олександр', 'Петро', 'Раїса',
             'Сергій', 'Тетяна', 'Уляна', 'Федір']

surnames_list = ['Смішкевич', 'Незнаєшкін', 'Гартунгус', 'Чобітко',
                 'Паліндромов', 'Веселийкіт', 'Ржавчак', 'Гомінчук',
                 'Жартович', 'Балабака', 'Шутюренко', 'Гуліверчук', 'Смішко',
                 'Куркуляндр', 'Балабуха', 'Хахоленко',
                 'Комічук', 'Забавко', 'Залупкін', 'Гуморко']

location_list = ['Липова Долина', 'Малий Любінь', 'Зелений Гай',
                 'Долина Сонця', 'Біле Озеро', 'Весела Річка',
                 'Ясна Поляна', 'Горяча Вода', 'Сокільниця',
                 'Кришталеве Озеро', 'Світла Долина', 'Щасливий Луг',
                 'Березова Рілля', 'Златоверха', 'Чисте Поле', 'Барвінкове',
                 'Лісовий Гай', 'Вишневе Поле', 'Ромашкове Поле']


# Cтворюю функція,яка генерує рандомну людину
def generate_random_person():
    persons = {
        'name': random.choice(name_list),
        'surname': random.choice(surnames_list),
        'location': random.choice(location_list),
    }
    return persons


generate_random_person()

# набір з рандомних людей які містяться в словнику
people_list = []
# словник з рандомно згенерованих людей
random_person = {}

# Цикл побудований на логіці,що він створює людей тільки на ту кількость імен
# яка є в name_list (так як ім'я -це буде головний ключ в нащому
# словнику)
for i in range(len(name_list)):
    random_person = generate_random_person()
    people_list.append(random_person)

# Зі створеного списку ми можемо дістати словник з 1 рандомної людини
random_person_from_list = random.choice(people_list)
print(random_person_from_list)

# Список зі словників рандомних людей
print(people_list)

