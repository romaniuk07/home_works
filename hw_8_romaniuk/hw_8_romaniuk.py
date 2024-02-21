from random import randint

# Створіть декоратор, який виводить в консоль ім'я функції, яку було викликано.
# Наприклад, створіть пару функцій для арифметичних операцій додавання і множення.
# При виклику цих функцій має повертатись результат операції і виводиться
# в консоль ім'я функції, яку було викликано.

def print_function_name(func):
    def wrapper(*args, **kwargs):
        print(f"Викликано функцію: {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper
@print_function_name
def add(a, b):
    return a + b

@print_function_name
def multiply(a, b):
    return a * b

result_add = add(3, 5)

print(f"Результат додавання: {result_add}")

result_multiply = multiply(2, 4)

print(f"Результат множення: {result_multiply}")


# Створіть за допомогою list comprehension список, в якому буде 100 елементів,
# і кожен із яких буде в границях від 1 до 10(для цього можна скористатись
# функцією randint із модуля random). Порахуйте кількість кожного елемента і виведіть в консоль


random_numbers = [randint(1, 10) for x in range(100)]

count_dict = {i: random_numbers.count(i) for i in set(random_numbers)}


for num, count in count_dict.items():
    print(f"Число {num}: {count} разів")


