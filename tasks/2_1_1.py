"""

Дан список со строками. Оставьте в этом списке только те строки, которые начинаются на http://.

"""

list_ = ['http://first-ever.ru/ ', 'http://e.ggtimer.com/', 'hello', 'world', 'http://eelslap.com/']

for i in list_:
    if i[0:7] == 'http://':
        print(i)
    else:
        continue