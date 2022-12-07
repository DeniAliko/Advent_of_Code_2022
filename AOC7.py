import sys
sys.setrecursionlimit(20954)

file = open("AOC7.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

def getSize(directory, file):
    size = 0
    for i in range(file.index(directory) + 2, len(file)):
        if file[i][0] == "d":
            size += getSize("$ cd " + file[i].replace("dir ", ""), file)
        elif file[i][0] == "$":
            break
        else:
            size += int(file[i].split(" ")[0])
    return size

file = open("AOC7.txt")
testCase = []
linesInTest = file.readlines()
for i in linesInTest:
    testCase.append(format(i.strip()))

sizes = []
for line in testCase:
    if line[0:4] == "$ cd":
        # sizes.append(getSize(line, inputFile))
        sizes.append(getSize(line, testCase))
        print("The Function was called!")

part1Answer = 0
for i in sizes:
    if i <= 100000:
        part1Answer += i

print(part1Answer)