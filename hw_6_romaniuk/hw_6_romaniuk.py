import re


# Задача 1:
# Напишіть програму яка перевіряє чи стрічка містить лише великі і малі
# літери, числа та нижнє підкреслення.^

password = "Password_123"
pattern = r"^\w+$"
result = re.match(pattern, password)
print(result)

# Задача 2:
# Напишіть програму, що видаляє область дужок в стрічці
# 		["example (.com)", "github (.com)", "stackoverflow (.com)"] ->
#
# 		example
# 		github
# 		stackoverflow


list_words = ["example (.com)", "github (.com)", "stackoverflow (.com)"]
pattern2 = r'\w+'


def delete_brakets(pattern2):
    sites = ''
    for word in list_words:
        result1 = re.findall(pattern2, word)
        names_of_site = result1[0]
        print(names_of_site)
        # Тут я вирішив заморочитися і зробити повну адресу
        domen = result1[1]
        sites += names_of_site + '.' + domen + '\n'

    print(sites)


delete_brakets(pattern2)

# Напишіть програму, що. вставляє пробіл перед великою літерою

words = 'HelloWordAndAllPeople'
uppercas = r"[A-Z]+"

result4 = re.sub(uppercas, r' \g<0>', words)
print(result4)
