import csv
import json
from datetime import datetime


def bus():
    file_name = 'data-398-2018-06-01.json'
    with open(file_name, 'r', encoding='CP1251') as file:
        databus = json.load(file)
        return databus


def underground():
    file_name = 'data-397-2018-03-27.json'
    with open(file_name, 'r', encoding='CP1251') as file:
        dataun = json.load(file)
        return dataun


def direction(databus, dataun):
    max_value = 0
    max_station = ''
    for row in dataun:
        x = row['geoData']['coordinates']
        station = row['NameOfStation']
        longitude1 = (x[0])
        latitude1 = (x[1])
        counter = 0
        for row1 in databus:
            coord = row1['geoData']['coordinates']
            longitude2 = (coord[0])
            latitude2 = (coord[1])
            res1 = longitude1 - longitude2
            if res1 < 0:
                res1 = -res1
            res2 = latitude1 - latitude2
            if res2 < 0:
                res2 = -res2
            if res1 <= 0.005 and res2 <= 0.008:
                counter += 1
        if counter > max_value:
            max_value = counter
            max_station = station

    print("Станция: ", max_station)
    print("Кол-во остановок: {}".format(max_value))


direction(bus(), underground())
