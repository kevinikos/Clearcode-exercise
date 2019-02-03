from datetime import datetime
import pycountry
import csv

def ReadFile():
    filename = 'clearcode-csv.csv'
    with open(filename, encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        Data = []
        for row in readCSV:
            Data.append(row[0:])
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

Data = ModifySubdiv()
for x in Data:
    print(x)

