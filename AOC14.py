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
                    points[((path[i][1]), y)] = "#"
                    rocks.append(((path[i][1]), y))
            else:
                for y in range(path[i][0], path[i + 1][0] - 1, -1):
                    points[((path[i][1]), y)] = "#"
                    rocks.append(((path[i][1]), y))
        elif path[i][0] == path[i + 1][0]:
            if path[i][1] < path[i+1][1]:
                for x in range(path[i][1], path[i + 1][1] + 1):
                    points[(x, (path[i][0]))] = "#"
                    rocks.append((x, (path[i][0])))
            else:
                for x in range(path[i][1], path[i + 1][1] - 1, -1):
                    points[(x, (path[i][0]))] = "#"
                    rocks.append((x, (path[i][0])))

# print(points)

xMin = 10000
yMin = 0
xMax = 0
yMax = 0
for point in points.keys():
    if point[1] > yMax:
        yMax = point[1]
    if point[0] > xMax:
        xMax = point[0]

for point in points.keys():
    if point[0] < xMin:
        xMin = point[0]

for y in range(yMin - 1, yMax + 2):
    for x in range(0, 2 * xMax):
        if (x, y) not in rocks and (y != yMax + 2):
            points[(x, y)] = "."

for x in range(-2 * xMax, 2 * xMax):
    points[(x, yMax + 2)] = "#"

# print(points)
# print(xMax, xMin, yMax, yMin)

class Sand:
    def __init__(self, x, y, stopped, voided):
        self.x = x
        self.y = y
        self.stopped = stopped
        self.voided = voided

    def move(self):
        # Go down
        if not self.stopped:
            if points[(self.x, self.y + 1)] == ".":
                self.y += 1
            elif points[(self.x - 1, self.y + 1)] == ".":
                self.y += 1
                self.x -= 1
            elif points[(self.x + 1, self.y + 1)] == ".":
                self.y += 1
                self.x += 1
            else:
                self.stopped = True

    def voidCheck(self):
        # if self.y >= yMax:
        #     self.voided = True
        # if self.x >= xMax:
        #     self.voided = True
        # if self.y <= 0:
        #     self.voided = True
        # if self.x <= xMin:
        #     self.voided = True

        if points[(500, 0)] == "O":
            self.voided = True

sandCount = 1
aSand = Sand(500, 0, False, False)
while aSand.voided == False:
    aSand.move()
    # print((aSand.x, aSand.y))
    # print(sandCount)
    aSand.voidCheck()
    if aSand.stopped:
        points[(aSand.x, aSand.y)] = "O"
        aSand.x = 500
        aSand.y = 0
        sandCount += 1
        aSand.stopped = False
    if aSand.voided:
        print(sandCount - 2)
        break