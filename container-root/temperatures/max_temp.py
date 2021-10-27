import csv

with open('max.csv', encoding='shift_jis') as csvfile:
    line = csv.reader(csvfile)
    for row in line:
        print(row)
