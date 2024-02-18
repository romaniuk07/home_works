from pathlib import Path
import re


# 4. Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) і повертає список словників виду
# {"date": date} у яких date - це дата з рядка (якщо є), Наприклад [{"date": "1st January 1919"},
# {"date": "8th February 1828"}, ...]

file_path = r"authors.txt"
file_name = Path(file_path).name

def get_athors(file_name):
    file = open(file_name, 'r')
    read_file = file.read()
    pattern = r'\d{1,2}\w{2} \w+ \d{4}'
    row = re.findall(pattern, read_file)
    list_of_dates = []
    for date in row:
        list_of_dates.append({'date': date})
    return list_of_dates

print(get_athors(file_name))