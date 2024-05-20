"""

Выведите в консоль все целые числа от 100 до 1.

"""

list_ = []
list2 = []
for i in range(1, 101):
    list_.append(i)
for k in list_[::-1]:
    list2.append(k)

print(*list2, sep="\n")
