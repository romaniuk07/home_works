# Створіть класс з описом будь-якої тварини. Додайте 1 static method

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def sound(self, sounds):
        return sounds

    @staticmethod
    def classification(paws):
        if paws == 4:
            return f'має {paws} лапки - це не павук'
        elif paws >= 5:
            return f'має {paws} лапок,обережно,може бути Бодя павук'
        return paws


# Створіть класс з описом будь-якої компанії чи організації. Додайте 1 classmethod

class Company:
    def __init__(self, name, industry):
        self.name = name
        self.industry = industry

    @classmethod
    def from_dict(cls, company_dict):
        return cls(company_dict['name'], company_dict['industry'])

    def get_info(self):
        return f"{self.name} - {self.industry}"


dog = Animal("Собака", "ссавець")
print(dog.sound(f'{dog.name} каже гав гав'))
print(dog.classification(4))

company_dict = {'name': 'Роги і Копита', 'industry': 'IT'}
google = Company.from_dict(company_dict)

print(google.get_info())
