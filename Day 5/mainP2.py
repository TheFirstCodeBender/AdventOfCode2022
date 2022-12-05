import re

'''
[F]         [L]     [M]            
[T]     [H] [V] [G] [V]            
[N]     [T] [D] [R] [N]     [D]    
[Z]     [B] [C] [P] [B] [R] [Z]    
[M]     [J] [N] [M] [F] [M] [V] [H]
[G] [J] [L] [J] [S] [C] [G] [M] [F]
[H] [W] [V] [P] [W] [H] [H] [N] [N]
[J] [V] [G] [B] [F] [G] [D] [H] [G]
 1   2   3   4   5   6   7   8   9 
'''
memory = [ ['J', 'H', 'G', 'M', 'Z', 'N', 'T', 'F'],
          ['V', 'W', 'J'],
          ['G', 'V', 'L', 'J', 'B', 'T', 'H'],
          ['B', 'P', 'J', 'N', 'C', 'D', 'V', 'L'],
          ['F', 'W', 'S', 'M', 'P', 'R', 'G'],
          ['G', 'H', 'C', 'F', 'B', 'N', 'V', 'M'],
          ['D', 'H', 'G', 'M', 'R'],
          ['H', 'N', 'M', 'V', 'Z', 'D'],
          ['G', 'N', 'F', 'H']
          ]


def SupplyStacks(instructions):
    answer = []

    for line in instructions:
        line = re.sub(r'[^0-9]', '', line)
        print(int(line[0] + line[1]))
        temp = []
        if len(line) == 3:
            move = int(line[0])
            From = int(line[1]) - 1
            to = int(line[2]) - 1
        else:
            move = int(line[0] + line[1])
            From = int(line[2]) - 1
            to = int(line[3]) - 1

        for stack in range(0,move):
            stack = stack - 1
            length = len(memory[From])
            temp.append(memory[From].pop())
        for item in range(0,move):
            memory[to].append(temp.pop())

    for item in memory:
        answer.append(item.pop())
    return answer





if __name__ == '__main__':
    file = open('input', 'r')
    elves = file.readlines()
    print(SupplyStacks(elves))