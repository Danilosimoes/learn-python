import csv

with open('people.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade: {}, Estado: {}'. format(*pessoa))