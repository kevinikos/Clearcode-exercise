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

Data = ModifyDate()

# germany = pycountry.countries.get(name='Mandiana')
# print(germany)
