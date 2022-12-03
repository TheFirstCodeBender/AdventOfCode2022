import re


def convertToPriority(item):
    if item.isupper():
        value = (ord(item) - 64) + 26
    else:
        value = ord(item) - 96
    return value


def RuckSackReorder(compartments):
    total = 0
    memory = {1: set(),
              2: set(),
              3: set()
              }
    count = 0
    for compartment in compartments:
        count += 1
        for item in compartment:
            if item not in memory[count]:
                memory[count].add(item)
        if count == 3:
            sameItems = memory[1].intersection(memory[2]).intersection(memory[3])
            sameItems.remove('\n')
            value = convertToPriority(sameItems.pop())

            total += value
            count = 0
            memory = {1: set(),
              2: set(),
              3: set()
              }

    return total


if __name__ == '__main__':
    file = open('input', 'r')
    elves = file.readlines()
    print(RuckSackReorder(elves))
