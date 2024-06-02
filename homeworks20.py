class Car:
    price = 1000000

    def horse_powers(self):
        horsepower = 212
        return horsepower


class Nissan(Car):
    price = 700000

    def horse_powers(self):
        horsepower = 190
        return 'Количество лошадинных сил: {}'.format(horsepower)


class Kia(Car):
    price = 900000

    def horse_powers(self):
        horsepower = 140
        return 'Количество лошадинных сил: {}'.format(horsepower)


print('Ниссан')
nissan = Nissan()
print('Стоимость машины:', nissan.price)
print(nissan.horse_powers())
print()
print('Киа')
kia = Kia()
print('Стоимость машины:', kia.price)
print(kia.horse_powers())



