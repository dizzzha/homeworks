first = 'Мама мыла раму'
second = 'Рамена мало было'


def get_advanced_writer(file_name):

    def write_everything(*data_set):
        f = open(file_name, 'w', encoding='utf8')
        for i in data_set:
            f.write(str(i))
            f.write('\n')
        f.close()

    return write_everything


class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        from random import choice
        return choice(self.words)


print(list(map(lambda x, y: x == y, first, second)))
"""
Lambda-функция: [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
"""

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
"""
Это строчка
['А', 'это', 'уже', 'число', 5, 'в', 'списке']
"""

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
"""
Примерный результат (может отличаться из-за случайности выбора):
Да
Да
Наверное
"""