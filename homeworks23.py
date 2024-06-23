file_name = '../7module/text.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    for line in file:
        print(line, end='')

# оператор with open(file_name...) отличается от file.close() тем, что file.close - это ручный метод закрытия.
# Рзработчик может попросту забыть использовать его, тем самым создав доп. нагрузку на память. Использование оператора
# with гарантирует закрытие файла
