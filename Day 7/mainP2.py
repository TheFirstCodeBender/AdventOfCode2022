import re


class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.dirs = []
        self.parent = parent  # Initialize
        self.memory = 0


def NoSpaceLeftInBrain(lines):
    memoryTree = Folder('/', None)
    currDir = memoryTree
    printing = False
    for line in lines:
        if 'cd' in line:
            if printing:
                printing = False
            if '..' in line:
                currDir = currDir.parent
            else:
                dir = Folder(line.split().pop(), currDir)
                currDir.dirs.append(dir)
                currDir = dir

                if memoryTree is None:
                    memoryTree = currDir

        if printing:
            if 'dir' not in line:
                fileMemorySize = line.split()[0]
                currDir.memory += int(fileMemorySize)
        if 'ls' in line:
            printing = True

    def TraverseFileSystem(fileSystem, answer = float('inf')):
        if len(fileSystem.dirs) == 0:
            if (40605258 - fileSystem.memory) <= 40000000:
                answer = min(answer, fileSystem.memory)
            return fileSystem.memory, answer

        for dir in fileSystem.dirs:
            totalMemory, answer = TraverseFileSystem(dir, answer)
            fileSystem.memory += totalMemory
        if (40605258 - fileSystem.memory) <= 40000000:
            answer = min(answer,fileSystem.memory)

        if fileSystem.name != '/':

            return fileSystem.memory, answer

        return fileSystem.memory, answer

    return TraverseFileSystem(memoryTree)

"Rough...🤣 (T.T)"
file = open('input', 'r')
elves = file.readlines()
print(NoSpaceLeftInBrain(elves))