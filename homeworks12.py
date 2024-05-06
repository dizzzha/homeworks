def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(1, 2, 3, 4)  # в консоле будет ошибка из-за того, что кол-во переданных
print_params(1, 2)           # параметров не совпадает с кол-вом параметров ф-ции

values_list = [13, 'Hello', False]
values_dict = {'a': 523, 'b': 'World', 'c': 2.35}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [32, 'Str']
print_params(*values_list_2, 42)
