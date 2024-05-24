import csv
with open("dataset.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)