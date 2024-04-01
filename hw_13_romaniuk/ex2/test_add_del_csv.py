import csv
import os

# 2 завдання. скористайтесь pytest. напишіть функцію, яка додає в csv один рядок. Напишіть функцію, яка видаляє з
# csv один рядок. напишіть два тести, які перевіряють відповідно чи додався рядок і чи він видалився.

test_file = 'test_file.csv'


def add_row_to_csv(file_path, row):
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)


def delete_row_from_csv(file_path, row_index):
    with open(file_path, 'r') as file:
        rows = list(csv.reader(file))

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row for index, row in enumerate(rows) if index != row_index)


def test_add_row_to_csv():
    if os.path.exists(test_file):
        os.remove(test_file)


    add_row_to_csv(test_file, ['John', 'Doe', 30])


    with open(test_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert ['John', 'Doe', '30'] in rows


def test_delete_row_from_csv():

    test_file = 'test.csv'

    with open(test_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([
            ['John', 'Doe', 30],
            ['Jane', 'Doe', 25],
            ['Alice', 'Smith', 35]
        ])

    # Delete a row
    delete_row_from_csv(test_file, 1)

    # Check if row is deleted
    with open(test_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert ['Jane', 'Doe', '25'] not in rows
