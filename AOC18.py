import queue

file = open("AOC18.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

cubes = []
for line in inputFile:
    cubes.append([int(line.split(",")[0]), int(line.split(",")[1]), int(line.split(",")[2])])

def getNeighbors(triple):
    upX = [triple[0] + 1, triple[1], triple[2]]
    downX = [triple[0] - 1, triple[1], triple[2]]
    upY = [triple[0], triple[1] + 1, triple[2]]
    downY = [triple[0], triple[1] - 1, triple[2]]
    upZ = [triple[0], triple[1], triple[2] + 1]
    downZ = [triple[0], triple[1], triple[2] - 1]
    return [upX, downX, upY, downY, upZ, downZ]

surfaceArea = 0
seen = []
for cube in cubes:
    seen.append(cube)
    surfaceArea += 6
    for neighbor in getNeighbors(cube):
        if neighbor in seen:
            surfaceArea -= 2

print(surfaceArea)

# part 2:
xMax = 0
xMin = 1000
yMax = 0
yMin = 1000
zMax = 0
zMin = 1000
for cube in cubes:
    if cube[0] > xMax:
        xMax = cube[0]
    if cube[0] < xMin:
        xMin = cube[0]
    if cube[1] > yMax:
        yMax = cube[1]
    if cube[1] < yMin:
        yMin = cube[1]
    if cube[2] > zMax:
        zMax = cube[2]
    if cube[2] < zMin:
        zMin = cube[2]

xMax += 2
xMin -= 2
yMax += 2
yMin -= 2
zMax += 2
zMin -= 2

biiigCube = []
for x in range(xMin, xMax + 1):
    for y in range(yMin, yMax + 1):
        for z in range(zMin, zMax + 1):
            biiigCube.append([x, y, z])

# Water BFS

def getNeighbors(triple):
    upX = [triple[0] + 1, triple[1], triple[2]]
    downX = [triple[0] - 1, triple[1], triple[2]]
    upY = [triple[0], triple[1] + 1, triple[2]]
    downY = [triple[0], triple[1] - 1, triple[2]]
    upZ = [triple[0], triple[1], triple[2] + 1]
    downZ = [triple[0], triple[1], triple[2] - 1]

    if triple[0] > xMax or triple[0] < xMin or triple[1] > yMax or triple[1] < yMin or triple[2] > zMax or triple[2] < zMin:
        upX = [triple[0], triple[1], triple[2]]
        downX = [triple[0], triple[1], triple[2]]
        upY = [triple[0], triple[1], triple[2]]
        downY = [triple[0], triple[1], triple[2]]
        upZ = [triple[0], triple[1], triple[2]]
        downZ = [triple[0], triple[1], triple[2]]

    return [upX, downX, upY, downY, upZ, downZ]

waterQueue = queue.Queue()
outsideArea = 0
visited = []
waterQueue.put((xMin, yMin, zMin))
while not waterQueue.empty():
    focusCube = waterQueue.get()
    if focusCube not in visited:
        visited.append(focusCube)
        if focusCube not in cubes:
            for neighbor in getNeighbors(focusCube):
                if neighbor in cubes:
                    outsideArea += 1
                    # print(outsideArea)
                else:
                    waterQueue.put(neighbor)

print(outsideArea)