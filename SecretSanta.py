import csv
import random
from copy import deepcopy
import EmailSender


# Python3 code here creating class
class People:
    def __init__(self, name, email):
        self.name = name
        self.email = email


# These people cannot get each other
exception = [
    ['Person1', 'Person3'],
    ['Person2', 'Person6']
]


def cannotMatch(x, y):
    for pair in exception:
        if (x == pair[0] and y == pair[1]) or (x == pair[1] and y == pair[0]):
            return True
    return False


def generatePairs(peopleList, shuffledList):
    x = deepcopy(peopleList)
    y = deepcopy(shuffledList)

    finalList = []

    for personFrom in x:
        for personTo in y:
            if personFrom.name == personTo.name or cannotMatch(personFrom.name, personTo.name):
                return False

            finalList.append({'from': personFrom, 'to': personTo})
            y.remove(personTo)
            break
    return finalList


def main():
    file = open('people.csv')
    csvreader = csv.reader(file)

    peopleList = []
    for row in csvreader:
        peopleList.append(People(row[0], row[1]))

    on = True
    while on:
        shuffledList = deepcopy(peopleList)
        random.shuffle(shuffledList)

        finalList = generatePairs(peopleList, shuffledList)

        if finalList:
            on = False

    for pair in finalList:
        EmailSender.send(pair['from'], pair['to'])


if __name__ == "__main__":
    main()
