# Temperature project
import numpy as np

def checkInt(check):
    try: int(check)
    except ValueError:
        return False
    else:
        return True


def checkFloat(check):
    try: float(check)
    except ValueError:
        return False
    else:
        return True


def tempStats():
    days = input("How many day's temperature? ")
    while not checkInt(check=days):
        print("Invalid input for number of days.")
        days = input("How many day's temperature? ")

    days = int(days)
    tempRecordings = np.array([])

    for i in range(1, days + 1):
        highTemp = input(f"Day {i}'s high temperature: ")
        while not checkFloat(highTemp):
            print("Not a valid input for temperature")
            highTemp = input(f"Day {i}'s high temperature: ")

        tempRecordings = np.append(tempRecordings, float(highTemp))
    average = sum(tempRecordings/len(tempRecordings))
    print("Average: ", average)
    count = 0
    for temp in tempRecordings:
        if temp > average:
            count += 1
    print("{} days(s) above average".format(count))


tempStats()