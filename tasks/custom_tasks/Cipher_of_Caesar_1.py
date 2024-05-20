str_ = "Hello world Za"
str_space = str_.split()
str_space2 = []
for i in str_space:
    str_space2.append(i)
    str_space2.append(' ')

alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper_symbols = [char for char in alphabet_upper]
alphabet_lower_symbols = [char for char in alphabet_lower]

new_str = []
for i in str_space2:
    if i == ' ':
        new_str.append(' ')
    for k in i:
        if k.isupper():
            pos = alphabet_upper_symbols.index(k) + len(i)
            if pos >= 26:
                pos -= 26
            list_ = alphabet_upper_symbols[pos]
            new_str.append(list_)
        elif k.islower():
            pos2 = alphabet_lower_symbols.index(k) + len(i)
            if pos2 >= 26:
                pos2 -= 26
            list2 = alphabet_lower_symbols[pos2]
            new_str.append(list2)

print(''.join(new_str))


