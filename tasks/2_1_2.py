"""

Дана некоторая строка. Найдите позицию первого нуля в строке.

"""

str_ = 'hello wor0ld'
s = 0
for i in str_:
    if i == ' ':
        s += 1
    if i == '0':
        print(str_.index('0')-s)
        break