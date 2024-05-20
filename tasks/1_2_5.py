# Даны два числа. Проверьте, что первые цифры этих чисел совпадают.

first_number = int(input())
second_number = int(input())
first_number = str(first_number)
second_number = str(second_number)

if first_number[0] == second_number[0]:
    print('Совпадают')
else:
    print("Не совпадают")
