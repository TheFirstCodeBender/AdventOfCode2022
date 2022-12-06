import re


def StartOfPacketMarker(lines):
    for line in lines:
        for char in range(0, len(line)):
            num = line[char: char + 4]
            numSet = set(num)
            if len(numSet) == len(num):
                return char + 4


if __name__ == '__main__':
    file = open('input', 'r')
    elves = file.readlines()
    print(StartOfPacketMarker(elves))
