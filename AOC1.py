file = open("AOC1.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

#for i in inputFile:
#    print(i)

organizedList = []
cacheList = []
for i in inputFile:
    if i != "":
        cacheList.append(i)
    if i == "":
        organizedList.append(cacheList)
        cacheList = []

cacheSum = 0
calorieSums = []
for i in range(0, len(organizedList)):
    for j in organizedList[i]:
        cacheSum += int(j)
    calorieSums.append(cacheSum)
    cacheSum = 0

a = max(calorieSums)
calorieSums.remove(max(calorieSums))
b = max(calorieSums)
calorieSums.remove(max(calorieSums))
c = max(calorieSums)

print(a+b+c)
