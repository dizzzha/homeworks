"""

Дан список с числами:

[1, 2, 3, 4, 5]
Найдите сумму квадратов элементов этого списка.

"""

list_ = [1, 2, 3, 4, 5]
list2 = []

for i in list_:
    s = i ** 2
    list2.append(s)

print(sum(list2))
