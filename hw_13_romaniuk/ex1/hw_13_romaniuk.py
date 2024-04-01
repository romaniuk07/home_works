import csv
import json

# 1 завдання. Напишіть адаптер, який конвертує json в csv.
class JSONToCSVConverter:
    def __init__(self):
        self.__data = []

    def read_json(self, filename: str):
        with open(filename, 'r') as json_file:
            self.__data = json.load(json_file)

    def write_csv(self, filename: str):
        if not self.__data:
            print("No data to write.")
            return

        with open(filename, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.__data[0].keys())
            writer.writeheader()
            writer.writerows(self.__data)

    def cleanup(self):
        self.__data = []


converter = JSONToCSVConverter()

converter.read_json('example.json')
converter.write_csv('test.csv')
