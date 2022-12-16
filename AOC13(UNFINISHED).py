file = open("AOC13.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

organizedList = []
cacheList = []
for i in inputFile:
    if i != "":
        cacheList.append(i)
    else:
        organizedList.append(cacheList)
        cacheList = []

print(organizedList[0])