from math import pi


class Figure:
    sides_count = 0
    filled = False
    r = None
    g = None
    b = None

    def __init__(self, color, *args):
        self.__color = color
        self.__sides = args
        if len(self.__sides) == 1:
            self.__sides = args
        else:
            sides_list = []
            for i in range(0, self.sides_count):
                sides_list.append(1)
            self.__sides = sides_list

    def get_color(self):
        return [*self.__color]

    @staticmethod
    def __is_valid_color(r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if r < 255 and g < 255 and b < 255:
                return True
            else:
                return False
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            return self.__color
        else:
            return self.__color

    def get_sides(self):
        return [*self.__sides]

    def __is_valid_sides(self, *args):
        for i in args:
            if i > 0 and self.sides_count == len(args):
                return True
            else:
                return False

    def set_sides(self, *args):
        if args is not None and len(args) == self.sides_count:
            self.__sides = args

    def __len__(self):
        if self.sides_count == 1:
            return int(*self.__sides)


class Circle(Figure):
    sides_count = 1
    __radius = 1 / pi

    def get_square(self):
        return pi * self.__radius * 2


class Triangle(Figure):
    sides_count = 3
    __height = None

    def get_square(self):
        return .5 * 3 * self.__height


class Cube(Figure):
    sides_count = 12
    __sides = []

    def __init__(self, color, *args):
        super(Cube, self).__init__(color, *args)
        self.__color = color
        sides_list = []
        if len(args) == 1:
            for i in range(0, self.sides_count):
                sides_list.append(*args)
            self.__sides = sides_list
        else:
            sides_list.append('Передайте один аргумент')
            self.__sides = sides_list

    def get_sides(self):
        return self.__sides

    def get_volume(self):
        return self.__sides[0] ** 3


# Код для проверки:


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
triangle1 = Triangle((200, 200, 100), 10, 6, 8)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
triangle1.set_color(56, 22, 99)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(triangle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
circle1.set_sides(15)  # Изменится
triangle1.set_sides(12)  # Изменится
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(circle1.get_sides())
print(triangle1.get_sides())
print(cube1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
"""
"""
"""
Выходные данные (консоль):
[55, 66, 77]
[56, 22, 99]
[222, 35, 130]
[15]
[1, 1, 1]
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
15
216

"""
