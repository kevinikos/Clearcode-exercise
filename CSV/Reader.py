from datetime import datetime
import pycountry
import csv

def ReadFile():
    try:
        filename = 'Example.csv'
        with open(filename, encoding="utf-8-sig") as csvfile:
            readCSV = csv.reader(csvfile, delimiter=';')
            Data = []
            for row in readCSV:
                Data.append(row[0:])
        return Data
    except FileNotFoundError as e:
        print(e)
        Data = []
        return Data

def ModifyDate():
    Data = ReadFile()
    for line in Data:
        try:
            DateFormat = datetime.strptime(line[0], '%m/%d/%Y').strftime('%Y-%m-%d')
            line[0] = DateFormat
        except ValueError as e:
            print(e)
    return Data

def ModifySubdiv():
    Data = ModifyDate()
    Subs = [] # subdivisions
    for sub in pycountry.subdivisions:
        Subs.append(sub)

    ShortSubs = [] # auxiliary list to check unknown subdivisions
    for x in Subs:
        ShortSubs.append(x.country.alpha_3)
        for y in Data:
            DataSub = y[1] # subdivision from Data list
            if x.name == DataSub:
                y[1] = x.country.alpha_3 # alpha_3 returns subdivision name
            else:
                continue

    for x in Data:
        if x[1] in ShortSubs:
            continue
        else:
            x[1] = "XXX" # replace unknown subdivisions to XXX
    return Data

def ModifyCTR():
    Data = ModifySubdiv()
    for x in Data:
        if x[3].endswith("%"): # remove '%' symbol if exist
            CTR = x[3][:-1]
            x[3] = int(float(CTR)*10) # changed string to float, and finally float to integer
        else:
            x[3] = int(float(x[3])*10)
    return Data

def SortData():
    Data = ModifyCTR()
    Data.sort(key=lambda x: x[0]) # sort by first element of list which is DATE
    for row in Data:
        print(row)

SortData()