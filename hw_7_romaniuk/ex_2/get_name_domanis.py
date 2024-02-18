from pathlib import Path
import re

# 2. Написати функцію, яка отримує у вигляді параметра ім'я файлу назви інтернет
# доменів (domains.txt) та повертає їх у вигляді списку рядків (назви повертати без крапки).

file_path = r"domains.txt"
file_name = Path(file_path).name


def get_name_domanis(file_name):
    raw_name_domains = open(file_name, 'r')
    domains = raw_name_domains.read().splitlines()
    pattern = r'\w+'
    domain_list = list()
    for word in domains:
        result = re.findall(pattern, word)
        domain_list += result
    return domain_list

print(get_name_domanis(file_name))