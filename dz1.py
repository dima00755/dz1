import random
import operator
from prettytable import PrettyTable
champ = {}
number = int(input("Введите количество команд:"))
for i in range(number):
    print("Введите название команды ", i + 1, ':')
    names = str(input())
    champ[i + 1] = names
k = 1
m = 1
o = 0
p = 0
results = {}
rev_results = {}
win = {}
lose = {}
draw = {}
goals = {}
missed = {}
points = {}
for p in range(1, number + 1):
    win[champ[p]] = 0
    lose[champ[p]] = 0
    draw[champ[p]] = 0
    goals[champ[p]] = 0
    missed[champ[p]] = 0
    points[champ[p]] = 0
for i in range(1, number + 1):
    for j in range(1 + k, number + 1):
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        if a > b:
            points[champ[i]] += 3
            win[champ[i]] += 1
            lose[champ[j]] += 1
        elif b > a:
            points[champ[j]] += 3
            lose[champ[i]] += 1
            win[champ[j]] += 1

        elif b == a:
            points[champ[i]] += 1
            points[champ[j]] += 1
            draw[champ[j]] += 1
            draw[champ[i]] += 1
        goals[champ[i]] += a
        missed[champ[i]] += b
        goals[champ[j]] += b
        missed[champ[j]] += a
        results[champ[i] + "-" + champ[j]] = str(a) + ':' + str(b)
        rev_results[champ[j] + "-" + champ[i]] = str(b) + ':' + str(a)
    k += 1
sorted_list = sorted(points.items(), key=lambda item: item[1], reverse=True)
sorted_bypoints_dict = dict(sorted_list)
a = sorted_bypoints_dict.keys()
a = list(a)
x = PrettyTable()
x.field_names = ["место", "команда", "победы", "поражения", "ничьи", "забито", "пропущено", "очки"]
for g in range(number):
    x.add_row([g + 1, a[g], win[a[g]], lose[a[g]], draw[a[g]], goals[a[g]], missed[a[g]], points[a[g]]])
print(x)
print('Список событий:')
p = 0
time_list = []
for r in range(1, number + 1):
    for t in range(1 + m, number + 1):
        o = t - m
        print(o + p, '.', champ[r] + "-" + champ[t], end=';  ')
        time_list.append(champ[r] + "-" + champ[t])
    p = p + (number - m)
    m += 1
print("Выход:", o + p)
print('\n')
print("Хотите узнать о событии подробнее Да(1)/Нет(0):")
to_exact = int(input())
j = 0
k = 0
list_number = []
for j in range(1, o + p + 1):
    list_number.append(j)
if (to_exact == 1):
    compare = 0
    while (compare != o + p):
        parametr = input("Введите название матча или его номер в списке событий:")
        if (parametr.isdigit()):
            parametr = int(parametr)
            compare = int(parametr)
            try:
                if parametr in list_number:
                    print(time_list[parametr - 1])
                    print(results[time_list[parametr - 1]])
            except IndexError:
                pass
            if parametr == o + p:
                print('выходим...')
            if parametr not in list_number:
                print('нет такой команды')
        else:
            try:
                print(results[parametr])
            except KeyError:
                try:
                    print(rev_results[parametr])
                except KeyError:
                    print("Нет такого события")