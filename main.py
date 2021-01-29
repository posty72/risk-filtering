import csv
import random

with open("input.csv", "r") as inputFile:
    with open("output.csv", "w") as outputFile:

        csv_reader = csv.reader(inputFile, delimiter=",")
        csv_writer = csv.writer(outputFile, delimiter=",")
        columns_to_check = range(3, 8)
        sample_size = 500
        rows_with_risk = []

        for row in csv_reader:
            has_risk = False
            for column in columns_to_check:
                if row[column] == '1':
                    has_risk = True

            if has_risk:
                rows_with_risk.append(row)

        for row in random.sample(rows_with_risk, 500):
            csv_writer.writerow(row)
