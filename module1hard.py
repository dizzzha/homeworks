"""

Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика,
а значением - его средний балл.

Вывод в консоль:
{'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}


"""

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
dict_ = {}
tuple_students = list(students)
tuple_students.sort()
tuple_students = tuple(tuple_students)
list_average = []

for k in grades:
    list_average.append(sum(k) / len(k))

index_count = 0
for i in tuple_students:
    dict_[tuple_students[index_count]] = list_average[index_count]
    index_count += 1
print(dict_)
