def add_everything_up(a, b):
    try:
        if isinstance(a, float) or isinstance(b, float):
            return round(a+b, 3)
        else:
            return a + b
    except TypeError:
        if isinstance(a, str) or isinstance(b, str):
            return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

# 123.456строка
# яблоко4215
# 130.456
