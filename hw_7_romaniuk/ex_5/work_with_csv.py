import csv


# 5.Створіть функцію, яка читає файл csv. Вона приймає назву файлу(str), повертає список рядків(list). Також створіть
# функцію, яка записує в файл данні. Вона приймає назву файлу(str), список рядків(list), які треба записать в файл.
# Нічого не повертає. Тепер за допомогою створених функцій спочатку створіть файл(3 рядків достатньо), потім прочитайте
# той-же файл, записавши рядки в змінну, потім додайте два рядки в змінну, і після цього запишіть ваші зміни в інший
# файл.

def read_csv(file_name):
    with open(file_name, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        rows = list()
        for row in csv_reader:
            rows.append(row)
    return rows


def write_csv(file_name2, data):
    with open(file_name2, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)



# Приклад використання
csv_file = "example.csv"

# Запис в файл
write_csv(csv_file, ['Petro', 25, 'Texas'])

# Читання з файлу
data = read_csv(csv_file)
print(data)

#  Додавання рядків
data.append(['Bob', 35, 'Nebraska'])
data.append(['Alice', 28, 'Ilinois'])
print('Додано 2 нових рядка', data)

# Запис у новий файл
new_csv_file = "example_new.csv"
write_csv(new_csv_file, data)

data2 = read_csv(new_csv_file)
print('Запис в новий фалй', data2)
