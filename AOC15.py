file = open("AOC15.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

sensors = []
beacons = []
distances = []
# inputFile = ["Sensor at x=2, y=18: closest beacon is at x=-2, y=15"]

# Parse into (x, y) for sensors, and beacons
for line in inputFile:
    cache1 = line.split(" ")[2]
    cache2 = cache1.split(",")[0]
    cache3 = int(cache2.split("=")[1])
    cacheX = cache3

    cache1 = line.split(" ")[3]
    cache2 = cache1.split(":")[0]
    cache3 = int(cache2.split("=")[1])
    cacheY = cache3

    sensors.append((cacheX, cacheY))

    cache1 = line.split(" ")[8]
    cache2 = cache1.split(",")[0]
    cache3 = int(cache2.split("=")[1])
    cacheX = cache3

    cache1 = line.split(" ")[9]
    cache2 = int(cache1.split("=")[1])
    cacheY = cache2

    beacons.append((cacheX, cacheY))

xMax = 0
for pair in sensors:
    if pair[0] > xMax:
        xMax = pair[0]
xMin = 100000000
for pair in sensors:
    if pair[0] < xMin:
        xMin = pair[0]

def getDistance(tuple1, tuple2):
    # print("Got a distance!")
    return abs(tuple1[0] - tuple2[0]) + abs(tuple1[1] - tuple2[1])

for i in sensors:
    distances.append(getDistance(i, beacons[sensors.index(i)]))

maxDist = max(distances)

# Part 1:

# 2000000
focusRow = 2000000
unAvail = 0
seen = []
for sensor in sensors:
    focusDistance = distances[sensors.index(sensor)]
    if sensor[1] >= focusRow and (sensor[1] - focusDistance) <= focusRow:
        for delX in range(sensor[0] - (focusDistance - (sensor[1] - focusRow)), sensor[0] + (focusDistance - (sensor[1] - focusRow) + 1)):
            if (delX, focusRow) not in beacons:
                seen.append((delX, focusRow))
                # print(seen)

    elif sensor[1] < focusRow and (sensor[1] + focusDistance) >= focusRow:
        for delX in range(sensor[0] - (focusDistance - (focusRow - sensor[1])), sensor[0] + (focusDistance - (focusRow - sensor[1]) + 1)):
            if (delX, focusRow) not in beacons:
                seen.append((delX, focusRow))
                # print(seen)

print(len(set(seen)))

# part 2:

# get all pairs of sensor ranges which are tangent:
pairs = []
for sensor in sensors:
    for otherSensor in sensors:
        if getDistance(sensor, otherSensor) == distances[sensors.index(sensor)] + distances[sensors.index(otherSensor)] + 2:
            pairs.append([sensor, otherSensor])

for pair in pairs:
    duplicate = pair
    duplicate.reverse()
    if duplicate in pairs:
        pairs.remove(duplicate)
print(pairs)

quadruple = []
for pair in pairs:
    quadruple.append(pair[0])
    quadruple.append(pair[1])

# x-delta = radius - deltaY
def getPerimeter(tuple, radius):
    perimeterPoints = []
    for y in range(tuple[1] - radius - 1, tuple[1] + radius + 1):
        perimeterPoints.append((tuple[0] - (radius - abs(tuple[1] - y)) + 1, y))
        perimeterPoints.append((tuple[0] + (radius - abs(tuple[1] - y)) + 1, y))
    return perimeterPoints

minRadius = 1000000000
for sensor in quadruple:
    if distances[sensors.index(sensor)] < minRadius:
        minRadius = distances[sensors.index(sensor)]

testPerim = getPerimeter(sensors[distances.index(minRadius)], minRadius)
part2Answer = 0
for i in testPerim:
    if getDistance(i, quadruple[0]) == distances[sensors.index(quadruple[0])] + 1:
        if getDistance(i, quadruple[1]) == distances[sensors.index(quadruple[1])] + 1:
            if getDistance(i, quadruple[2]) == distances[sensors.index(quadruple[2])] + 1:
                if getDistance(i, quadruple[3]) == distances[sensors.index(quadruple[3])] + 1:
                    print(i)
                    print(i[0] * 4000000 + i[1])