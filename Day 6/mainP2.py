import re


def StartOfPacketMarker(lines):
    for line in lines:
        for char in range(0, len(line)):
            num = line[char: char + 14]
            numSet = set(num)
            if len(numSet) == len(num):
                return char + 14


if __name__ == '__main__':
    file = open('input', 'r')
    elves = file.readlines()
    print(StartOfPacketMarker(elves))
