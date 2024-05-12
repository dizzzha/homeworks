"""

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

Выходные данные (консоль):
99

Примечания (рекомендации):
Весь подсчёт должен выполняться одним вызовом функции.
Рекомендуется применить рекурсивный вызов функци, для каждой внутренней структуры.
Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
Для определения типа данного используйте функцию isinstance.

"""


def calculate_structure_sum(*args):
    s = 0
    list_ = [*args]
    for item in list_:
        if isinstance(item, str):
            s += len(item)
        elif isinstance(item, int):
            s += item
        elif isinstance(item, set):
            for value in item:
                if isinstance(value, str):
                    s += len(value)
                elif isinstance(value, int):
                    s += value
        elif isinstance(item, list):
            calculate_structure_sum(*args)
            for value in item:
                if isinstance(value, str):
                    s += len(value)
                elif isinstance(value, int):
                    s += value
        elif isinstance(item, tuple):
            for value in item:
                if isinstance(value, str):
                    s += len(value)
                elif isinstance(value, int):
                    s += value
        elif isinstance(item, dict):
            for key, values in item.items():
                print(key, values)
        else:
            print('DK')
    return s


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
