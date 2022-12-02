import re


def Max_Calories(Elves):
    # Since you know the Length of the stack you can set each number to 0.
    top3 = {'1st': 0,
            '2nd': 0,
            '3rd': 0}

    number_pattern = "^\\d+$"
    totalCal = 0
    maxCal = 0

    for calorie in Elves:
        calorie = re.search(number_pattern, calorie)

        if calorie is not None:
            calorie = calorie.group(0)
            totalCal += int(calorie)

        else:
            # if it is greater than third item in stack you KNOW it must be top 3
            if totalCal > top3['3rd']:
                for place, cals in top3.items():
                    if totalCal > cals:
                        top3[place] = totalCal
                        # In case the totalCal is greater than the 1st or 2nd cals you want to shift it down one
                        totalCal = cals
            totalCal = 0

    return top3['1st'] + top3['2nd'] + top3['3rd']


if __name__ == '__main__':
    file = open('inputQ1', 'r')
    elves = file.readlines()
    print(Max_Calories(elves))
