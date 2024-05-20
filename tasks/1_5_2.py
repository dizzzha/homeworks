"""

Найдите сумму всех целых четных чисел в промежутке от 1 до 100.

"""

summa = 0

for i in range(1, 101):
    if i % 2 == 0:
        summa += i

print(summa)
