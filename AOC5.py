import time
file = open("AOC5.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

#print(inputFile)

organizedList = []
for i in inputFile:
    if i[6] == " ":
        organizedList.append([int(i[5]), int(i[12]), int(i[17])])
    if i[6] != " ":
        organizedList.append([int(i[5]+i[6]), int(i[13]), int(i[18])])

#print(organizedList)
testList = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]

organizederList = []
tempCount = 0
for i in organizedList:
    while tempCount < i[0]:
        organizederList.append([i[1], i[2]])
        tempCount += 1
    if tempCount == i[0]:
        tempCount = 0

#print(organizederList)

# Starting Stacks:
stack1 = ["F", "L", "M", "W"]
stack2 = ["B", "Z", "V", "M", "F"]
stack3 = ["H", "V", "R", "S", "L", "Q"]
stack4 = ["F", "S", "V", "Q", "P", "M", "T", "J"]
stack5 = ["L", "S", "W"]
stack6 = ["F", "V", "P", "M", "R", "J", "W"]
stack7 = ["J", "Q", "C", "P", "N", "R", "F"]
stack8 = ["V", "H", "P", "S", "Z", "W", "R", "B"]
stack9 = ["B", "M", "J", "C", "G", "H", "Z", "W"]
stackList = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]
#print(stackList)
def rearrange(x, y):
    cacheCrate = stackList[x-1][len(stackList[x-1])-1]
    stackList[x-1].pop()
    stackList[y-1].append(cacheCrate)

for i in organizederList:
    rearrange(i[0], i[1])

part1Answer = ""
for item in stackList:
    part1Answer += item[-1]

print(part1Answer)

# Part 2:
stack1 = ["F", "L", "M", "W"]
stack2 = ["B", "Z", "V", "M", "F"]
stack3 = ["H", "V", "R", "S", "L", "Q"]
stack4 = ["F", "S", "V", "Q", "P", "M", "T", "J"]
stack5 = ["L", "S", "W"]
stack6 = ["F", "V", "P", "M", "R", "J", "W"]
stack7 = ["J", "Q", "C", "P", "N", "R", "F"]
stack8 = ["V", "H", "P", "S", "Z", "W", "R", "B"]
stack9 = ["B", "M", "J", "C", "G", "H", "Z", "W"]
stackList = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]
#print(stackList)

def arrayReverse(list):
    arrayReverseCache = []
    for i in range(1, len(list)+1):
        arrayReverseCache.append(list[-i])
    return arrayReverseCache

def newRearrange(n, x, y):
    cacheClump = []
    for i in range(1, n+1):
        cacheClump.append(stackList[x-1][-i])
    cacheClump = arrayReverse(cacheClump)
    thisothercounter = 0
    while thisothercounter < n:
        stackList[x-1].pop()
        thisothercounter += 1
    stackList[y-1].extend(cacheClump)

    # Visualisation
    # anInput = input("")
    # print(stackList[0])
    # print(stackList[1])
    # print(stackList[2])
    # print(stackList[3])
    # print(stackList[4])
    # print(stackList[5])
    # print(stackList[6])
    # print(stackList[7])
    # print(stackList[8])
    # print("--------------------------------------------")

for i in organizedList:
    newRearrange(i[0], i[1], i[2])

part2Answer = ""
for item in stackList:
    part2Answer += item[-1]
print(part2Answer)
