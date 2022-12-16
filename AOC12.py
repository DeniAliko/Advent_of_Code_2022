import queue
file = open("AOC12.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

organizedList = []
cacheList = []
for y in range(len(inputFile) - 1, -1, -1):
    for x in range(0, len(inputFile[y])):
        cacheList.append(inputFile[y][x])
    organizedList.append(cacheList)
    cacheList = []

# too lazy to change things back to inputFile lol
organizedList.reverse()

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

end = (20, 132)
start = (20, 0)

def getNeighbors(tuple):
    y = tuple[0]
    x = tuple[1]
    neighbors = []
    if y > 0:
        if letters.index(organizedList[y][x]) >= letters.index(organizedList[y - 1][x]) - 1:
            neighbors.append((y - 1, x))
    if x > 0:
        if letters.index(organizedList[y][x]) >= letters.index(organizedList[y][x - 1]) - 1:
            neighbors.append((y, x - 1))
    if y < len(organizedList) - 1:
        if letters.index(organizedList[y][x]) >= letters.index(organizedList[y + 1][x]) - 1:
            neighbors.append((y + 1, x))
    if x < len(organizedList[y]) - 1:
        if letters.index(organizedList[y][x]) >= letters.index(organizedList[y][x + 1]) - 1:
            neighbors.append((y, x + 1))

    return neighbors

nodeQueue = queue.Queue()
visited = []
parents = {}
done = False
prevNode = start
currentChildren = []
nodeQueue.put(start)
while not nodeQueue.empty():
    focusNode = nodeQueue.get()
    if focusNode not in visited:
        visited.append(focusNode)
        # print(focusNode)
        if focusNode == end:
            done = True
        for neighbor in getNeighbors(focusNode):
            if neighbor not in visited:
                parents[neighbor] = focusNode
                nodeQueue.put(neighbor)

# print(len(visited))
# print(parents)

stepCount = 0
def getParents(point):
    global stepCount
    stepCount += 1
    if parents[point] != start:
        print(parents[point])
        return getParents(parents[point])

#All I know is my answer was off by two and i dont know why
getParents(end)
# print(end)
# print(stepCount)
# print(start)

# part dos:

def newNeighbors(tuple):
    y = tuple[0]
    x = tuple[1]
    neighbors = []
    if y > 0:
        if letters.index(organizedList[y-1][x]) >= letters.index(organizedList[y][x]) - 1:
            neighbors.append((y - 1, x))
    if x > 0:
        if letters.index(organizedList[y][x-1]) >= letters.index(organizedList[y][x]) - 1:
            neighbors.append((y, x - 1))
    if y < len(organizedList) - 1:
        if letters.index(organizedList[y+1][x]) >= letters.index(organizedList[y][x]) - 1:
            neighbors.append((y + 1, x))
    if x < len(organizedList[y]) - 1:
        if letters.index(organizedList[y][x+1]) >= letters.index(organizedList[y][x]) - 1:
            neighbors.append((y, x + 1))

    return neighbors

start = end
nodeQueue = queue.Queue()
visited = []
parents = {}
done = False
prevNode = start
currentChildren = []
destinationA = (0, 0)
nodeQueue.put(start)
while not nodeQueue.empty():
    focusNode = nodeQueue.get()
    if focusNode not in visited:
        visited.append(focusNode)
        # print(focusNode)
        if organizedList[focusNode[0]][focusNode[1]] == "a":
            destinationA = focusNode
            break
        for neighbor in newNeighbors(focusNode):
            if neighbor not in visited:
                parents[neighbor] = focusNode
                nodeQueue.put(neighbor)

stepCount = 0
def getParents(point):
    global stepCount
    stepCount += 1
    if parents[point] != start:
        print(parents[point])
        return getParents(parents[point])

getParents(destinationA)
print(stepCount)
print(destinationA)