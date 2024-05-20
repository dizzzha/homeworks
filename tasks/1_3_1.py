# Дана строка. Если в этой строке более одного символа, выведите в консоль предпоследний символ этой строки.

usr_str = str(input())
length_usr_str = len(usr_str)

if length_usr_str > 1:
    print(usr_str[-2])