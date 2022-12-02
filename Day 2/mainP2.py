import re

P1 = {'A': 'Rock',
      'B': 'Paper',
      'C': 'Scissors'}

Strategy = {'X': 'lose',
            'Y': 'draw',
            'Z': 'win'}

Values = {'Rock': 1,
          'Paper': 2,
          'Scissors': 3}
MapToLosing = {'Rock': 'Scissors',
               'Paper': 'Rock',
               'Scissors': 'Paper'}
MapToVictory = {'Rock': 'Paper',
                'Paper': 'Scissors',
                'Scissors': 'Rock'}


def RPS(p1, strategy):
    if strategy == 'draw':
        return p1
    if strategy == 'win':
        return MapToVictory[p1]
    if strategy == 'lose':
        return MapToLosing[p1]


def StrategyGuide(rounds):
    totalScore = 0
    for round in rounds:
        roundClean = re.sub(r'[^a-zA-Z]', '', round)
        p1 = P1[roundClean[0]]
        strategy = Strategy[roundClean[1]]
        p2 = RPS(p1, strategy)
        win = 0

        value = Values[p2]
        if strategy == 'win':
            win = 6
        elif strategy == 'draw':
            win = 3

        totalScore += value + win

    return totalScore


if __name__ == '__main__':
    file = open('inputQ2', 'r')
    rounds = file.readlines()
    print(StrategyGuide(rounds))
