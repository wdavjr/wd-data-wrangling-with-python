import csv

csv_file = open("data-text.csv", "r")
reader = csv.DictReader(csv_file)

for row in reader:
    print(row)
