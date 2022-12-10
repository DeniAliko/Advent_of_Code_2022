file = open("AOC9.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

headX = 0
headY = 0
tailX = 0
tailY = 0
tailX2 = 0
tailY2 = 0
tailX3 = 0
tailY3 = 0
tailX4 = 0
tailY4 = 0
tailX5 = 0
tailY5 = 0
tailX6 = 0
tailY6 = 0
tailX7 = 0
tailY7 = 0
tailX8 = 0
tailY8 = 0
tailX9 = 0
tailY9 = 0
visited = [(0, 0)]

def tailMove(hX, hY, tX, tY):

    deltaX = hX - tX
    deltaY = hY - tY
    followX = 0
    followY = 0

    if deltaX == 1 and deltaY == 2 or deltaX == 2 and deltaY == 1:
        followX = 1
        followY = 1
    elif deltaX == -1 and deltaY == 2 or deltaX == -2 and deltaY == 1:
        followX = -1
        followY = 1
    elif deltaX == 1 and deltaY == -2 or deltaX == 2 and deltaY == -1:
        followX = 1
        followY = -1
    elif deltaX == -1 and deltaY == -2 or deltaX == -2 and deltaY == -1:
        followX = -1
        followY = -1
    # I forgot about these following 4 cases entirely :P
    elif deltaX == 2 and deltaY == 2:
        followX = 1
        followY = 1
    elif deltaX == 2 and deltaY == -2:
        followX = 1
        followY = -1
    elif deltaX == -2 and deltaY == 2:
        followX = -1
        followY = 1
    elif deltaX == -2 and deltaY == -2:
        followX = -1
        followY = -1
    elif deltaY == 2:
        followY = 1
    elif deltaY == -2:
        followY = -1
    elif deltaX == 2:
        followX = 1
    elif deltaX == -2:
        followX = -1

    return (followX, followY)

def move(command):
    global headX
    global headY
    global tailX
    global tailY
    global tailX2
    global tailY2
    global tailX3
    global tailY3
    global tailX4
    global tailY4
    global tailX5
    global tailY5
    global tailX6
    global tailY6
    global tailX7
    global tailY7
    global tailX8
    global tailY8
    global tailX9
    global tailY9

    direction = command.split(" ")[0]
    magnitude = int(command.split(" ")[1])

    for count in range(magnitude):

        if direction == "D":
            headY -= 1
        elif direction == "U":
            headY += 1
        elif direction == "R":
            headX += 1
        elif direction == "L":
            headX -= 1

        tail1New = (tailX + tailMove(headX, headY, tailX, tailY)[0], tailY + tailMove(headX, headY, tailX, tailY)[1])
        tailX = tail1New[0]
        tailY = tail1New[1]
        tail2New = (tailX2 + tailMove(tailX, tailY, tailX2, tailY2)[0], tailY2 + tailMove(tailX, tailY, tailX2, tailY2)[1])
        tailX2 = tail2New[0]
        tailY2 = tail2New[1]
        tail3New = (tailX3 + tailMove(tailX2, tailY2, tailX3, tailY3)[0], tailY3 + tailMove(tailX2, tailY2, tailX3, tailY3)[1])
        tailX3 = tail3New[0]
        tailY3 = tail3New[1]
        tail4New = (tailX4 + tailMove(tailX3, tailY3, tailX4, tailY4)[0], tailY4 + tailMove(tailX3, tailY3, tailX4, tailY4)[1])
        tailX4 = tail4New[0]
        tailY4 = tail4New[1]
        tail5New = (tailX5 + tailMove(tailX4, tailY4, tailX5, tailY5)[0], tailY5 + tailMove(tailX4, tailY4, tailX5, tailY5)[1])
        tailX5 = tail5New[0]
        tailY5 = tail5New[1]
        tail6New = (tailX6 + tailMove(tailX5, tailY5, tailX6, tailY6)[0], tailY6 + tailMove(tailX5, tailY5, tailX6, tailY6)[1])
        tailX6 = tail6New[0]
        tailY6 = tail6New[1]
        tail7New = (tailX7 + tailMove(tailX6, tailY6, tailX7, tailY7)[0], tailY7 + tailMove(tailX6, tailY6, tailX7, tailY7)[1])
        tailX7 = tail7New[0]
        tailY7 = tail7New[1]
        tail8New = (tailX8 + tailMove(tailX7, tailY7, tailX8, tailY8)[0], tailY8 + tailMove(tailX7, tailY7, tailX8, tailY8)[1])
        tailX8 = tail8New[0]
        tailY8 = tail8New[1]
        tail9New = (tailX9 + tailMove(tailX8, tailY8, tailX9, tailY9)[0], tailY9 + tailMove(tailX8, tailY8, tailX9, tailY9)[1])
        tailX9 = tail9New[0]
        tailY9 = tail9New[1]

        if tail9New not in visited:
            visited.append(tail9New)

for command in inputFile:
    move(command)

# print(visited)
print(len(visited))