def personal_sum(*args):
    result = 0
    incorrect_data = 0
    for arg in args:
        for i in arg:
            try:
                result += i
            except TypeError:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return result, incorrect_data


def calculate_average(*args):
    if isinstance(*args, int):
        return None
    try:
        tuple_func = personal_sum(*args)
        return tuple_func[0] / (len(*args) - tuple_func[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        return f'В numbers записан некорректный тип данных'


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать

"""

Некорректный тип данных для подсчёта суммы - 1
Некорректный тип данных для подсчёта суммы - ,
Некорректный тип данных для подсчёта суммы -
Некорректный тип данных для подсчёта суммы - 2
Некорректный тип данных для подсчёта суммы - ,
Некорректный тип данных для подсчёта суммы -
Некорректный тип данных для подсчёта суммы - 3
Результат 1: 0
Некорректный тип данных для подсчёта суммы - Строка
Некорректный тип данных для подсчёта суммы - Ещё Строка
Результат 2: 2.0
В numbers записан некорректный тип данных
Результат 3: None
Результат 4: 26.5

"""
