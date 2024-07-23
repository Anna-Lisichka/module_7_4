team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'


if score1 > score2 or score1 == score2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

# Использование %:

print('В команде %(name)s участников: %(team)d %(i)s' % {'name': team1, 'team': team1_num, 'i': '!'})
print('Итого сегодня в командах участников: %(t1)d %(a)s %(t2)d %(i)s'
      % {'t1': team1_num, 'a': 'и', 't2': team2_num, 'i': '!'})

# Использование format():

print('Команда {} решила задач: {}'.format(team2, score2))
print('Команда {} решили задачи за: {}{}'.format(team2, team2_time, ' c!'))

# Использование f-строк:

print(f'Команды решили {score1} и {score2} задачи.')
print(f'Результат битвы: {result} ')
print(f'Сегодня было решено {tasks_total} задачи, в среднем по {45.2} на задачу')
print(f'Сегодня было решено {score1 + score2} задачи, в среднем по'
      f' {round(((team1_time + team2_time)/tasks_total), 2)} на задачу')
