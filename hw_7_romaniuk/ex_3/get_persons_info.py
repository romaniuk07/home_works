from pathlib import Path

# 3. Написати функцію, яка отримує у вигляді параметра ім'я файлу (names.txt)
# і повертає список усіх прізвищ з нього. Кожен рядок файлу містить номер,
# прізвище, країну. Файл створити власноруч і записати туди дані

file_path = r"names.txt"
file_name = Path(file_path).name


def get_last_names(file_name):
    last_names = []

    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            last_name = line.strip().split()[-1]
            last_names.append(last_name)
    return last_names


last_names = get_last_names(file_name)
print("Список прізвищ:")
print(last_names)
