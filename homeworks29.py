def apply_all_func(int_list, *functions):
    res = {}
    for elm in functions:
        res[elm.__name__] = elm(int_list)
    return res


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

"""

Вывод на консоль:
{'max': 20, 'min': 6} 
{'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}

"""