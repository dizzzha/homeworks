"""

Создайте новую функцию def test... с произвольным числом параметров разного типа, функция должна распечатывать
эти параметры внутри своего тела
Создайте рекурсивную функцию, которая будет считать факториал от числа n, n - передается в параметре
В ответ прикрепите получившийся файл main.py

"""


def test(*args, **kwargs):
    print(*args, *kwargs)


test(1, 2, 3, False, 'str', a=1, b=2)


def recursive_func(n):
    if n == 0:
        return 1
    else:
        return n * recursive_func(n-1)


print(recursive_func(5))

