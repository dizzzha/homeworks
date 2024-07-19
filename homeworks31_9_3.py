first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(frst) - len(scnd) for frst, scnd in zip(first, second) if len(frst) != len(scnd))
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))

print(list(first_result))
print(list(second_result))

"""

Вывод в консоль:
[1, 2]
[False, False, True]

"""
