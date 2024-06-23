from pprint import pprint

file_name = '../7module/text.txt'
file = open(file_name, mode='rb')  # mode (режим): чтение бинарное
file_content = file.read()
file.close()
pprint(file_content)
