from time import time, sleep
from threading import Thread


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf8') as f:
        for num in range(1, word_count+1):
            f.write(f'Какое-то слово № {num}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start = time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_end = time()
res_time_usual = time_end - time_start
print(f'Работа потоков {res_time_usual}')

thr_time_start = time()
thr_1 = Thread(target=wite_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=wite_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=wite_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=wite_words, args=(100, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()
thr_time_end = time()
res_time_thr = thr_time_end - thr_time_start

print(f'Работа потоков {res_time_thr}')
"""

Вывод на консоль:
Завершилась запись в файл example1.txt
Завершилась запись в файл example2.txt
Завершилась запись в файл example3.txt
Завершилась запись в файл example4.txt
Работа потоков 0:00:34.003411 # Может быть другое время
Завершилась запись в файл example5.txt
Завершилась запись в файл example6.txt
Завершилась запись в файл example8.txt
Завершилась запись в файл example7.txt
Работа потоков 0:00:20.071575 # Может быть другое время

"""