import queue

file = open("AOC17test.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

air = queue.Queue()
for char in inputFile[0]:
    air.put(char)

occupied = []
for i in range(1, 8):
    occupied.append([i, 0])

class Rock:
    def __init__(self, positions, stopped):
        self.positions = positions
        self.stopped = stopped

    def moveDown(self):
        moveImpossible = False
        for coord in self.positions:
            if [coord[0], coord[1] - 1] in occupied:
                moveImpossible = True
        if not moveImpossible:
            for coord in self.positions:
                coord[1] -= 1
        elif moveImpossible:
            self.stopped = True
            for coord in self.positions:
                if coord not in occupied:
                    occupied.append(coord)

    def moveSide(self, char):
        moveImpossible = False
        if char == ">":
            for coord in self.positions:
                if coord[0] == 7 or [coord[0] + 1, coord[1]] in occupied:
                    moveImpossible = True
            for coord in self.positions:
                if not moveImpossible:
                    coord[0] += 1
            
        elif char == "<":
            for coord in self.positions:
                if coord[0] == 1  or [coord[0] - 1, coord[1]] in occupied:
                    moveImpossible = True
            for coord in self.positions:
                if not moveImpossible:
                    coord[0] -= 1

def yMaxCheck():
    global yMax
    for coord in occupied:
        if coord[1] > yMax:
            yMax = coord[1]
    # print(yMax)

count = 0
yMax = 0

dashRock = [[3, yMax + 4], [4, yMax + 4], [5, yMax + 4], [6, yMax + 4]]
plusRock = [[3, yMax + 5], [4, yMax + 4], [5, yMax + 5], [4, yMax + 6], [4, yMax + 5]]
ellRock = [[3, yMax + 4], [4, yMax + 4], [5, yMax + 4], [5, yMax + 5], [5, yMax + 6]]
tallRock = [[3, yMax + 4], [3, yMax + 5], [3, yMax + 6], [3, yMax + 7]]
squareRock = [[3, yMax + 4], [3, yMax + 5], [4, yMax + 4], [4, yMax + 5]]
startPositions = [dashRock, plusRock, ellRock, tallRock, squareRock]

while count < 2026:

    dashRock = [[3, yMax + 4], [4, yMax + 4], [5, yMax + 4], [6, yMax + 4]]
    plusRock = [[3, yMax + 5], [4, yMax + 4], [5, yMax + 5], [4, yMax + 6], [4, yMax + 5]]
    ellRock = [[3, yMax + 4], [4, yMax + 4], [5, yMax + 4], [5, yMax + 5], [5, yMax + 6]]
    tallRock = [[3, yMax + 4], [3, yMax + 5], [3, yMax + 6], [3, yMax + 7]]
    squareRock = [[3, yMax + 4], [3, yMax + 5], [4, yMax + 4], [4, yMax + 5]]
    startPositions = [dashRock, plusRock, ellRock, tallRock, squareRock]
    testRock = Rock(startPositions[count % 5], False)

    while not testRock.stopped:
        currentMove = air.get()
        if air.empty():
            for char in inputFile[0]:
                air.put(char)
        testRock.moveSide(currentMove)
        testRock.moveDown()

    yMaxCheck()
    count += 1

cacheList = []
for i in range(yMax - 10, yMax + 1):
    for coord in occupied:
        if coord[1] == i:
            cacheList.append(coord)
    print(cacheList)
    cacheList = []

for coord in occupied:
    if coord[1] == yMax:
        cacheList.append(coord)
print("Top layer:")
print(cacheList)

cacheList = []
for coord in occupied:
    if coord[1] == 1:
        cacheList.append(coord)
print("Bottom layer:")
print(cacheList)

print("Remaining Queue:")
print(air.qsize())

print("Last shape:")
print(testRock.positions)

# Part deux

count = 0
yMax = 0
foundCycle = False

def cycleCheck():
    global foundCycle
    if air.qsize() == 0 and count % 5 == 0:
        print("Found cycle, size", count)
        foundCycle = True

# while not foundCycle:

#     dashRock = [[3, yMax + 4], [4, yMax + 4], [5, yMax + 4], [6, yMax + 4]]
#     plusRock = [[3, yMax + 5], [4, yMax + 4], [5, yMax + 5], [4, yMax + 6], [4, yMax + 5]]
#     ellRock = [[3, yMax + 4], [4, yMax + 4], [5, yMax + 4], [5, yMax + 5], [5, yMax + 6]]
#     tallRock = [[3, yMax + 4], [3, yMax + 5], [3, yMax + 6], [3, yMax + 7]]
#     squareRock = [[3, yMax + 4], [3, yMax + 5], [4, yMax + 4], [4, yMax + 5]]
#     startPositions = [dashRock, plusRock, ellRock, tallRock, squareRock]
#     testRock = Rock(startPositions[count % 5], False)

#     while not testRock.stopped:
#         currentMove = air.get()
#         cycleCheck()
#         if air.empty():
#             for char in inputFile[0]:
#                 air.put(char)
#         testRock.moveSide(currentMove)
#         testRock.moveDown()
#     print("Rock stopped!", count)

#     yMaxCheck()
#     count += 1

# print("ymax:", yMax)

# cacheList = []
# for coord in occupied:
#     if coord[1] == yMax:
#         cacheList.append(coord)
# print("Top layer:")
# print(cacheList)

# cacheList = []
# for coord in occupied:
#     if coord[1] == 1:
#         cacheList.append(coord)
# print("Bottom layer:")
# print(cacheList)