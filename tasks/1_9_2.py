"""

Дан словарь с числами:

{
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
}
Увеличьте каждое число из словаря в 2 раза:

{
	'a': 2,
	'b': 3,
	'c': 6,
	'd': 8,
}

"""

dict_ = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}

# for i in dict_:
#     c = dict_.get(i)
#     dict_[i] = c * 2

for i in dict_:
    dict_.update({i: dict_.get(i) * 2})

print(dict_)
