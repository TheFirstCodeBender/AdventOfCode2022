
import re


def Max_Calories(Elves):
    number_pattern = "^\\d+$"
    totalCal = 0
    maxCal = 0
    for calorie in Elves:
        calorie = re.search(number_pattern, calorie)
        if calorie is not None:
            calorie = calorie.group(0)
            totalCal += int(calorie)
        else:
            if totalCal > maxCal:
                maxCal = totalCal
            totalCal = 0

    return maxCal


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open('inputQ1', 'r')
    elves = file.readlines()
    print(Max_Calories(elves))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
