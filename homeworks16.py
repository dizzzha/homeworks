class House:

    def __init__(self):
        self.numberOfFloors = 10


house = House()

for i in range(1, house.numberOfFloors + 1):
    print('Текущий этаж равен:', i)

# class Robot:
#
#     def __init__(self):
#         self.name = 'Robot1'
#         self.color = 'Gray'
#         self.speed = '0 км/ч'
#         self.height = {True: 2, 'abc': 3, 123: 4}
#
#     def go(self):
#         self.height = False
#         self.speed = '50 км/ч'
#
#
# robot = Robot()
# robot.temperature = 50
# print('color', robot.color)
# print('speed', robot.speed)
# print('height', robot.height)
# print('temperature', robot.temperature)
# del robot.temperature
# robot.go()
# print('speed', robot.speed)
# print('height', robot.height)

"""
class House:

    def __init__(self, param_height_home):
        self.numberOfFloors = 10
        self.heightHome = param_height_home

house1 = House(param_height_home=3)

class House:  # шаблон объекта. Класс используется, как шаблон для создания объектов
    ...
    тело класса 
    ...
    
numberOfFloors - атрибут (св-во)
param_height_home - параметр метода
10 - значение

house1 = House(param_height_home=3) 
3 - значение передаваемое в параметр param_height_home метода __init__
"""

# human1 = {
#     'Левая нога': True,
#     'Правая нога': True,
#     'Левая рука': True,
#     'Правая рука': True,
#     'Возраст': 15,
#     'Рост': 172,
#     'Вес': 120
# }
#
# human2 = {
#     'Левая нога': True,
#     'Правая нога': True,
#     'Левая рука': True,
#     'Правая рука': True,
#     'Возраст': 18,
#     'Рост': 175,
#     'Вес': 60
# }
#
# human3 = {
#     'Левая нога': True,
#     'Правая нога': True,
#     'Левая рука': True,
#     'Правая рука': True,
#     'Возраст': 12,
#     'Рост': 173,
#     'Вес': 70
# }
#
# human4 = {
#     'Левая нога': True,
#     'Правая нога': True,
#     'Левая рука': True,
#     'Правая рука': True,
#     'Возраст': 12,
#     'Рост': 133,
#     'Вес': 20
# }
#
#
# class Human:
#
#     def __init__(self, age, height, weight):
#         self.left_foot = True
#         self.left_hand = True
#         self.right_foot = True
#         self.right_hand = True
#         self.human_age = age
#         self.human_height = height
#         self.human_weight = weight
#
#
# man1 = Human(age=15, height=172, weight=120)
# man2 = Human(age=18, height=190, weight=60)
# man3 = Human(age=12, height=150, weight=70)
# man4 = Human(age=15, height=130, weight=30)
