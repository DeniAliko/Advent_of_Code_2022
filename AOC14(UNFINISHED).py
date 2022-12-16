file = open("AOC14.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

points = {}

parsedPaths = []
break1 = []
break2 = []
for path in inputFile:
    break1 = path.split(" -> ")
    for pair in break1:
        break2.append([int(pair.split(",")[1]), int(pair.split(",")[0])])
    parsedPaths.append(break2)
    break2 = []

rocks = []

for path in parsedPaths:
    for i in range(0, len(path) - 1):
        if path[i][1] == path[i + 1][1]:
            if path[i][0] < path[i + 1][0]:
                for y in range(path[i][0], path[i + 1][0] + 1):
                    points[(y, (path[i][1]))] = "#"
                    rocks.append((y, (path[i][1])))
            else:
                for y in range(path[i][0], path[i + 1][0] - 1, -1):
                    points[(y, (path[i][1]))] = "#"
                    rocks.append((y, (path[i][1])))
        elif path[i][0] == path[i + 1][0]:
            if path[i][1] < path[i+1][1]:
                for x in range(path[i][1], path[i + 1][1] + 1):
                    points[((path[i][0]), x)] = "#"
                    rocks.append(((path[i][0]), x))
            else:
                for x in range(path[i][1], path[i + 1][1] - 1, -1):
                    points[((path[i][0]), x)] = "#"
                    rocks.append(((path[i][0]), x))

xMin = 0
yMin = 0
xMax = 0
yMax = 0
for point in points.keys():
    if point[0] > yMax:
        yMax = point[0]
    if point[1] > xMax:
        xMax = point[1]

for y in range(yMin, yMax + 1):
    for x in range(xMin, xMax + 1):
        if (y, x) not in rocks:
            points[(y, x)] = "."

# print(points)
# print(xMin, xMax, yMin, yMax)

class Sand:
    def __init__(self, y, x, stopped, voided):
        self.x = x
        self.y = y
        self.stopped = False
        self.voided = False

    def move(self):
        # Go down
        if not self.stopped:
            if points[(self.y + 1, self.x)] == ".":
                self.y += 1
            elif points[(self.y + 1, self.x - 1)] == ".":
                self.y += 1
                self.x -= 1
            elif points[(self.y + 1, self.x + 1)] == ".":
                self.y += 1
                self.x += 1
            else:
                self.stopped = True
                points[(self.y, self.x)] = "O"

    def voidCheck(self):
        if self.y >= yMax:
            self.voided = True
        if self.x >= xMax:
            self.voided = True
        if self.y <= 0:
            self.voided = True
        if self.x <= 0:
            self.voided = True

stationarySands = 0
sands = []
sands.append(Sand(0, 500, False, False))
while sands[len(sands) - 1].stopped == False:
    sands[len(sands) - 1].voidCheck()
    if sands[len(sands) - 1].voided == True:
        print(stationarySands)
        break
    if not sands[len(sands) - 1].voided:
        sands[len(sands) - 1].move()
    if sands[len(sands) - 1].stopped:
        stationarySands += 1
        sands.append(Sand(0, 500, False, False))
        print("New sand created!")