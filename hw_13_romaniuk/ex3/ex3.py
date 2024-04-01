from abc import ABC, abstractmethod


# 3. опишіть частину функціоналу замовлення в ресторані. OrderPart класс має метод, що повертає певне блюдо.
# Можуть бути різніблюда, наприклад Risotto, Pasta, Pizza, які наслідуються від одного
# батьківського абстрактного класу Dish(Factory).
class Dish(ABC):
    @abstractmethod
    def get_description(self):
        pass


class Risotto(Dish):
    def get_description(self):
        return "Risotto"


class Pasta(Dish):
    def get_description(self):
        return "Pasta"


class Pizza(Dish):
    def get_description(self):
        return "Pizza"


class OrderPart:
    def __init__(self):
        self.dish_factory = None

    def set_dish_factory(self, dish_factory):
        self.dish_factory = dish_factory

    def get_dish(self):
        if self.dish_factory is None:
            return None
        return self.dish_factory.get_description()



order_part = OrderPart()


order_part.set_dish_factory(Risotto())
print(order_part.get_dish())

order_part.set_dish_factory(Pasta())
print(order_part.get_dish())

order_part.set_dish_factory(Pizza())
print(order_part.get_dish())
