import csv

#print csv field names
with open('stops.csv', 'r', encoding='cp1251') as file:
    reader = csv.DictReader(file, delimiter=";")
    r_heads = reader.fieldnames #список полей
    print(r_heads)

#print value for a key
