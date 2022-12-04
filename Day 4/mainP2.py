


def PairContainers(pairs):
    count = 0
    for pair in pairs:
        pair = pair.replace('\n', '')
        pair = pair.split(',')
        pair1 = pair[0].split('-')
        pair2 = pair[1].split('-')
        lower1 = int(pair1[0])
        upper1 = int(pair1[1])
        lower2 = int(pair2[0])
        upper2 = int(pair2[1])

        if lower2 <= lower1 <= upper2 or lower1 <= lower2 <= upper1:
            count += 1
        else:
            print(pair)

    return count


if __name__ == '__main__':
    file = open('input', 'r')
    elves = file.readlines()
    print(PairContainers(elves))