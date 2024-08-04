def all_variants(text):
    from itertools import combinations
    for i in range(1, len(text)+1):
        for comb in combinations(text, i):
            yield ''.join(comb)


a = all_variants("abc")
for i in a:
    print(i)


"""
Вывод на консоль:
a
b
c
ab
bc
abc
"""
