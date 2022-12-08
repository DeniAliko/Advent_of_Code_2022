file = open("AOC7.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

organizedList = []
currentPath = ""
accumulating = False
currentPathSum = 0
for i in inputFile:
    if i[0] == "$" and accumulating:
        organizedList.append([currentPath, currentPathSum, 0])
        accumulating = False
    if i[0:4] == "$ cd":
        if i == "$ cd ..":
            currentPathSum = 0
            currentPath = currentPath[0:currentPath.rindex(">")]
        else:
            currentPath += ">" + i.split(" ")[2]
    if i[0:4] == "$ ls":
        currentPathSum = 0
        accumulating = True
    if i.split(" ")[0].isnumeric():
        currentPathSum += int(i.split(" ")[0])
organizedList.append([currentPath, currentPathSum, 0])
# print(organizedList)

currentChildren = []
for i in organizedList:
    for j in organizedList:
        if j[0].startswith(i[0]):
            i[2] += j[1]

part1Answer = 0
for i in organizedList:
    if i[2] <= 100000:
        part1Answer += i[2]
print(part1Answer)

neededSpace = 30000000 - (70000000 - organizedList[0][2])
deletable = []
for i in organizedList:
    if i[2] >= neededSpace:
        deletable.append(i[2])
print(min(deletable))