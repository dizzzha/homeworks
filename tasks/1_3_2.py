# Даны два целых числа. Проверьте, что первое число без остатка делится на второе.

first_number = int(input())
second_number = int(input())

if first_number % second_number == 0:
    print('Без остатка')
else:
    print('С остатком')