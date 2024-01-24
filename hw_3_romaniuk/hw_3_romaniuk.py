list_entered = []

words = ['add', 'earliest', 'latest', 'longest', 'shortest', 'exit']
while True:
    entered = input("Введіть команду: ").lower()
    if entered != '':
        if entered in words:
            if entered == 'add':
                enter_add = input("Введіть нотатку: ")
                if enter_add != '':
                    list_entered.append(enter_add)
                    print(f"Нотатку {enter_add} додано.Актуальний список "
                          f"{list_entered}")
                else:
                    print('Ви нічого не ввели')
            elif entered == 'earliest':
                print(f"від найстарішої до найновішої: {list_entered}")
            elif entered == 'latest':
                print(f"від найновішої до найстарішої: {list_entered[
                                                        ::-1]}")
            elif entered == 'longest':
                print(f"від найдовшої нотатки до найкоротшої: "
                      f"{sorted(list_entered, key=len, reverse=True)}")
            elif entered == 'shortest':
                print(f'від найкоротшої нотатки до найдо'
                      f'вшої: {sorted(list_entered, key=len)}')
            elif entered == 'exit':
                confirm_exit = input("Якщо ви хочете вийти - напишіть y або "
                                     "yes: ")
                if (confirm_exit.lower() == 'y' or confirm_exit.lower() ==
                        'yes'):
                    print('Бувай здоровий')
                    break
        else:
            print(f'Введена команда не підтримується')
    else:
        print(f'Ви нічого не ввели')

# Я трішки вийшов за межі завдання і модифікував,а саме додав умови:
#     *додав перевірку на введення команди яких немає в умовах програми
#     *додав перевірку на введенння пустої строки
#     *додав функцію .lower() для інпуту
#     *додав підтвердження для виходу пісдя введення команди exit
