def is_prime(func):
    def wrapper(a, b, c):
        res = func(a, b, c)
        list_ = []
        condition = res > 1 and res % 1 == 0 and res % res == 0
        for i in range(1, res+1):
            if res % i == 0:
                list_.append(i)
        if len(list_) == 2 and condition:
            return f'Простое\n{res}'
        elif len(list_) > 2 and condition:
            return f'Составное\n{res}'
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)  #  Простое
result2 = sum_three(1, 5, 1)  #  Простое
result3 = sum_three(2, 3, 3)  #  Составное
print(result)
print(result2)
print(result3)
"""
Результат консоли:
Простое
11
"""
