from datetime import datetime
import csv

filename = 'clearcode-csv.csv'
with open(filename, encoding="utf8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    Data = []
    for row in readCSV:
        Data.append(row[0:3])

for line in Data:
    try:
        DateFormat = datetime.strptime(line[0], '%m/%d/%Y').strftime('%Y-%m-%d')
        line[0] = DateFormat
    except ValueError as e:
        print(e)

print(Data)