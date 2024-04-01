class TrainCar:
    def __init__(self, number):
        self.number = number
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < 10:
            self.passengers.append(passenger)
        else:
            print("Train car is full.")

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        return f'"traincar": "{self.number}"\n' + '\n'.join(
            [f'"passenger_name": "{passenger["name"]}",\n"destination": "{passenger["destination"]}",\n"place": {passenger["place"]}' for passenger in self.passengers]
        ) + '\n'


class Train:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def __len__(self):
        return len(self.cars)

    def __str__(self):
        return '\n'.join([str(car) for car in self.cars])



# Створення вагонів
car1 = TrainCar(1)
car1.add_passenger({"name": "John Dow", "destination": "Name of station", "place": 1})
car1.add_passenger({"name": "Alex Dowson", "destination": "Name of station", "place": 2})

car2 = TrainCar(2)
car2.add_passenger({"name": "Alice", "destination": "Another station", "place": 1})
car2.add_passenger({"name": "Bob", "destination": "Another station", "place": 2})

# Створення потягу та додавання вагонів
train = Train()
train.add_car(car1)
train.add_car(car2)

# Виведення інформації про вагони та потяг
print(train)
print(f"Number of cars without locomotive: {len(train)}")
