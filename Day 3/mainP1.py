import re


def RuckSackReorder(compartments):
    total = 0
    memory = set()
    for compartment in compartments:
        length = len(compartment)
        mid = length // 2
        for item in range(0,mid):
            memory.add(compartment[item])

        for item in range(mid,length):

            if compartment[item] in memory:
                if compartment[item].isupper():
                    value = (ord(compartment[item]) - 64) + 26
                else:
                    value = ord(compartment[item]) - 96
                memory.clear()

        total += value
    return total



if __name__ == '__main__':
    file = open('input', 'r')
    elves = file.readlines()
    print(RuckSackReorder(elves))


