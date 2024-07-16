class Car:

    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self._is_valid_vin(vin)
        self.__is_valid_numbers(numbers)

    def _is_valid_vin(self, vin_number):
        self.__vin_number = vin_number
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер', self.__vin_number)
        elif not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера', self.__vin_number)
        else:
            return True

    def __is_valid_numbers(self, numbers):
        self.__numbers = numbers
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров', self.__numbers)
        elif not len(numbers) == 6:
            raise IncorrectCarNumbers('Неверная длина номера', self.__numbers)
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message, vin_number):
        self.message = message
        self.__vin_number = vin_number


class IncorrectCarNumbers(Exception):
    def __init__(self, message, numbers):
        self.message = message
        self.__numbers = numbers


# Код для проверки
try:
    first = Car('Model1', 1000000, 'f123dj')  # Model1 успешно создан
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')  # Неверный диапазон для vin номера
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')  # Неверная длина номера
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')


