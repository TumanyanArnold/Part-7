team1_num = 5   # Команда "Мастера"
team2_num = 6   # Команда "Волшебники"

score_1 = 40
score_2 = 42

team1_time = 18015.2
team2_time = 19016.3



print("В команде Мастера кода участников: %s !" % team1_num)
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))

print("Команда Волшебники данных решила задач {} !".format(score_2))
print("Волшебники данных решили задачи за {} c".format(team1_time))

print(f"Команды решили {score_1} и {score_2} задачи.")

# Исход соревнований!
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_num:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_num:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья'
print(f"Результат битвы: {challenge_result}")

task_total = score_1 + score_2
time_avg = (team1_time + team2_time) / task_total

print(f"Сегодня было решено {task_total} задач, в среднем по {time_avg:.2f} секунды на задачу!")