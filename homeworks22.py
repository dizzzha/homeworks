from pprint import pprint

file_name = '../7module/text.txt'
file = open(file_name, mode='rb')
file_content = file.read()
pprint(file_content)
file.close()
