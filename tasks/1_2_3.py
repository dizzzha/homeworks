# Дано число. Выведите в консоль сумму первой и последней цифры этого числа.

user_number = int(input())
user_number = str(user_number)
first_symbol = user_number[0]
last_symbol = user_number[-1]

print(int(first_symbol) + int(last_symbol))