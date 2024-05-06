def test(a=True, b=1, c='Str'):
    print(a, b, c)


test()


def recursive_func(n):
    if n == 0:
        return 1
    else:
        return n * recursive_func(n-1)


print(recursive_func(5))

