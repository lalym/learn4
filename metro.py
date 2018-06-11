import json
from datetime import datetime

date = datetime.now()
curdate = datetime.strftime(date, '%d.%m.%Y')
print(curdate)

with open('data-397-2018-03-27.json', 'r', encoding='cp1251') as file:
    data = json.load(file)
    rep = 0
    repnow = 0


    print('Ремонт эскалаторов: \n')
    for r in data:
        if len(r['RepairOfEscalators']) != 0:
            print(r['NameOfStation'])
            rep += 1

        elif r['RepairOfEscalators'] == curdate:
            print(r['NameOfStation'])
            repnow += 1

    print('Current RepairOfEscalators: \n', repnow)
    print('RepairOfEscalators: \n', rep)