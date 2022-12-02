import re


def RPS(p1, p2):
    if p1 == p2:
        return None
    if p1 == 'Rock' and p2 == 'Scissors':
        return False
    elif p1 == 'Scissors' and p2 == 'Paper':
        return False
    elif p1 == 'Paper' and p2 == 'Rock':
        return False
    else:
        return True


def Max_Calories(rounds):
    P1 = {'A': 'Rock',
          'B': 'Paper',
          'C': 'Scissors'}

    P2 = {'X': 'Rock',
          'Y': 'Paper',
          'Z': 'Scissors'}

    Values = {'Rock': 1,
              'Paper': 2,
              'Scissors': 3}

    totalScore = 0
    for round in rounds:
        roundClean = re.sub(r'[^a-zA-Z]', '', round)
        p1 = P1[roundClean[0]]
        p2 = P2[roundClean[1]]
        win = 0
        wonRound = RPS(p1, p2)

        value = Values[p2]
        if wonRound:
            win = 6
        elif wonRound is None:
            win = 3

        totalScore += value + win

    return totalScore



if __name__ == '__main__':
    file = open('inputQ2', 'r')
    elves = file.readlines()
    print(Max_Calories(elves))


