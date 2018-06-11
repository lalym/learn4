import csv

with open('stops.csv', 'r', encoding='cp1251') as file:
    reader = csv.DictReader(file, delimiter=";")
    counter = {}

    for row in reader:
        counter.setdefault(row['Street'], 0)
        counter[row['Street']] += 1
    x = sum(counter.values())  # summa vsex ostanovok
    print("Кол-во остановок: {}".format(x))

    v = list(counter.values())  # list iz kluchey
    k = list(counter.keys())  # list iz znacheniy
    max_k = k[v.index(max(v))]  # ulica
    print("Улица, на которой больше всего остановок: {}".format(max_k))
    max_v = v[v.index(max(v))]  # ostanovki
    print("Количество остановок на улице {} : {}".format(max_k, max_v))
