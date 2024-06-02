class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000

    def horse_powers(self, horsepower):
        return horsepower


class Nissan(Car, Vehicle):
    price = 650000
    vehicle_type = 'sedan'

    def horse_powers(self, horsepower):
        return horsepower


car = Nissan()
print(f'Тип кузова: {car.vehicle_type}, Стоимость машины: {car.price} руб.')
print(f'Число лошадинных сил: {car.horse_powers(123)}')

