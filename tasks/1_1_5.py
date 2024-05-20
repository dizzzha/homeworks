# Даны два слова. Проверьте, что первые буквы этих слов совпадают.

first_word = str(input())
second_word = str(input())

if first_word[0:1] == second_word[0:1]:
    print('Совпадает, бро')
else:
    print('Не совпадает')