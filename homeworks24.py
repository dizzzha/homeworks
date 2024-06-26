# Общая информация о командах и их результатах
team1_num = 6
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

# Использование %
print('В команде Мастера кода участников: %d' % team1_num)
print('В команде Волшебники данных участников: %d' % team2_num)

print('Итого сегодня в командах участников: %(team1_num)d и %(team2_num)d' % {
    "team1_num": team1_num, "team2_num": team2_num
})


# Использование format()
print('')
print('Команда Мастера кода решила задач: {}'.format(score_1))
print('Команда Волшебники данных решила задач: {}'.format(score_2))

print('Мастера кода решили задачи за {}'.format(team1_time))
print('Волшебники данных решили задачи за {}'.format(team2_time))


# Использование f-строк
print('')
print(f'Команды решили {score_1} и {score_2} задач.')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья'
print(f'Результат битвы: победа команды {challenge_result}')



