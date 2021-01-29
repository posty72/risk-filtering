import csv
import random


def weightedRandom(weight):
    num = random.randint(0, 100)

    if num > weight:
        return 0
    else:
        return 1


with open("input-seed.csv", "w") as inputFile:

    spamwriter = csv.writer(inputFile, delimiter=",")

    for i in range(1, 1000000):
        if i == 1:
            spamwriter.writerow(["hi", "hi", "hi", 10, 20, 30, 50, 100])

        else:
            weight = 20
            hundred = weightedRandom(weight)
            fifty = hundred or weightedRandom(weight)
            thirty = fifty or weightedRandom(weight)
            twenty = thirty or weightedRandom(weight)
            ten = twenty or weightedRandom(weight)

            spamwriter.writerow(
                [
                    "irrelevant",
                    "irrelevant",
                    "irrelevant",
                    hundred,
                    fifty,
                    thirty,
                    twenty,
                    ten,
                ]
            )
