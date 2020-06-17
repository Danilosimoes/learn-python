import csv

with open('people.csv') as file:
    reader = csv.DictReader(file)

    count = 0

    for row in reader:
        print(row['Maria'])

        if count > 5:
            break

        count += 1

