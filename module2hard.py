"""

Составьте алгоритм, используя циклы, чтобы в независимости от введённого числа n (от 3 до 20) программа выдавала
нужный пароль result, для одного введённого числа.

Все пароли для чисел от 3 до 20 (для сверки):
3 - 12
4 - 13
5 - 1423
6 - 121524
7 - 162534
20 - 13141911923282183731746416515614713812911
"""

num = int(input('Введите число: '))
list_ = []
added_pairs = set()

for i in range(1, 21):
    for k in range(1, 21):
        if i == k:
            continue
        if num % (i + k) == 0 and (i, k) not in added_pairs:
            list_.append(i)
            list_.append(k)
            added_pairs.add((i, k))
            added_pairs.add((k, i))
print(num, ' - ', *list_, sep="")


