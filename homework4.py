immutable_var = 1, 'Hello, world', 1.05, True
print('Immutable tuple: ', immutable_var)

# immutable_var[:1] = 'Hey'
# print(immutable_var) # В консоле выдаст ошибку в связи с тем, что кортеж - неизменяемый объект

mutable_list = [2, 'Hello, world'], 1.05, False
mutable_list[0][1] = 'Hey'
print('Mutable list: ', mutable_list)
