import queue

fileName = "AOC22.txt"
file = open(fileName)
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip("\n")))

if fileName == "AOC22.txt":
    position = (51, 1)
    sideLength = 50
    inputDirections = "42R43L25R29R48L44R4L30R4L46L14L13R45L12R11L47L32R12L6L16L36L10R37L40L10L23L2L13R31L3L5R30L5L22L12R33L1L2R29R43R12R1L19L20L49R30R14L44R14R31R25L38L40R4L10L21L23L45L36R13R6L16R20L6L12L21R7L47R45R19L7R37R34R14R37R45R5R10R24L4L45L1L6L10R10L43R34R31L32L17L12R39R22L46L26R46R1L18R44R50L42L48R15L28L33R34L48R23R9R15R5R46R30R4L17R36R16L16R28R7L10L47L37L11R50R8L26R17R34L36L25R31R30R33L36L26L31L39R39R14R34L31L2L1L23L39R11R27L10L41R29R11L2L50L4R7R36L31R28L7L33L44L31R46R13R41L10R50R14L1L47R22R10L2R22L34L24R39R37L29R29L6R43L50L43R20R41L41L41R49L35R4L28R32L40L48R28L5R41R5R10R1R5L26R11R30L21R26R30R47R27L1L13R21R18L15L38R2R15R44R27L10L32L29L9L41L17L29R14R41R27L26R24R24R7L24R6R38L7R17L47L2R26R16L34L35L20R21L6R39L3R16L23L42L1R42L4R10L7L16L47L12R39R27R40L48L32R32R22L43R3L12R19R42R5L12R36L10R27L25L33R27R22L35L36L35L38L50L11L31R45L43L41L15L25L23L29R12L34L9R20L43R21L50L19L19L21R21R41L15L33R42R44R26R23L34L41L35L34R34R41L19R29L20L4L30L15R5L24R34R37L34L35R20R8R41L1L20L46L46L14R29R13R36R31R47R46R36R19L49L27L38L29L47L3L30R15R24L2R28L11L50R3R47R22L48L40L2R12R14L8R9R41R2L9R9L45L37R41R50L18R11L50L19L6R40R7R24L5R26R22L23R23R11L3L7R26R20R43R19R24R46L47R9L24R37L14L20R4R40R48R38L21L20R12L10R31L29L32L43L8L11L4R6R4R41L6L8L3L34L14L14R20L4L25L45R31R29L34R50L10L7L42L34L29L25R22R45R39L28L44L37R18R45R34R7R33L14L31L9R9L45R12R31R1R45L8L45L14R18R2R40L29R29L38L33R6R38L40L46R47L9L21R13L16R45R24R15R11R38L6R27L3R24R12L22R43L32L8L15R40R2R6L40L34R31R8R39L32R45L34R25L26R3L44L28R1R48L50L29R11R4L45R43L8L34L15R12L34R39L32R45R28R20R35R14L13L21R17L27R29R46L46R48L38R3L14L10R40R1L1R25L39L43R37L19L38L18R28L12L7L9L49L34L8L35R31R18R32R11L14R15L39L39R30R7L25R37R16L34L29L2R39R31R6L4R41L28L36L47L1L6L43L36L23L16L34R45L8L29L20L45L39L2L19L35R47R10L27L47L9R10R12R11L25L25L19L36L6R45L25R35R30L40R42R1R44R13R13R40R30L48L13R40L39R18L49L17L20R33R43L40L21R34L20L20R50R32L28R39L39R5R22R9R20L33R41L23L43L39R49L37L3R5R2L43L4R32R49L30R4L30L25R40L9L6R17R41L38L44R38R22L47L19R10R1L13R43L13R22R46R24R43L15R35L35R10L44L7R31L16R17L24R9L14L7L30R4L11L49L5R46L32R28R35L7R34L44R26R2R11L48R11R41L16R21L44L9L17L8R14L49R16L30L15L21L6L27R25L25L26L41R33L10R10R16L19L33R44R38L1R6R40R18L14L10L28L35L47L36R6L17R49R23L37L45L32R12R21L49L20R36L36R8L7L44R38R16L2R20L13L19R25L25L31L16L3L1R31L44R45L20R14R23R25R2L16L47L21R31R37L46R29R40R18L23R10R15L8L33R9R10L9L3L47R22L31R10L17L5R14L39L33R30L7L15R45R18R17R17R49R11L31R36L30L50R3R31L38L19R14L22R40L48L40R30L28R32R5R24L9R19R21R12L14R41L3R50L46R26R24L45R5L2L49L11R50R34R8R12L23R31L37L26L32L25R46L28R35R10L2R31L38L41R37L22L29L25R23R42R32L2R3R44R50R26L13L36R9L10R16L1R14L50L46R20R33R28R20L40L6R34L33R2L25R29L18L28R3L15L37R20L42R4L16R30R46L35L18R2L31L16R24R24R34R22R10L27R38R16R30R7R30L27R10R17L18L20L5R21L43L26L42L41R4L45R8L20L31R43L19L2R18L35R7R42R32L15L21R35L44L43L7R23R35L36L45L49R16R13R35R34R11R39L35R21R34L30R48R35L20L8R43R7R30L34R35R13R15L10L30R36L7L2L47R39L36R31L23R44R15L20R21R5R2R50L9L29L12L7L38R19R10R33R10R15R35L17L11R9L26R7L48L25R21L34L26R47L3R5L22L27R8L15L46L1L34L27L8L37R5R24L33R17R50L33L16R7R19R38R22R6L48L38L9R8R3R41L22L11R38L49R5R16R2L15L11L15R8R37R48R42L17L9R20L24R27R7R31L19R3R30R42L24R14R47L39L26R45R19R7R18L11R30R23L46R46R4R10L13L20R25R41L39L44R48R15R36R9R27R4L19R36R45R11R42R28R33R50R42R27R49L44R43R12R37R31L9R20R37L50R2L41L16R43L19R41R44R23R23L1R39L39L11L32L1L17R17L4R48L32R39R37L3R4R17R19L38R15R5R41R40L48L8R13L23L11L21L6R18L50R4L21R23R25L33R38R4R46L16R12L21L22R26R16L11L42R23R21R47L27R5L27R39L36L17R2L19R14R45R20R41R42R46L26R23R32R32R1L17R38L15R42R29R20R17R3L42L29L38R7L7L46R30R26R37R21R23L14L23R22R40R8L16L27R17R12R32R22R48L4L8L16R9R25R42R35R15L49R47L13R49R20L36R35L34R4L12L22L49R26L45R41R37L3L29R21R3L23R43R19L5R12R43L16R31L19R28R26R8L41R11L22R28L18R31L24R13R2L27R4L22L27L49R25R8R31R8R49R45R15R12R42L20R32L10L35L37R7R14L20L32R41L26L48R17R4R39R47R12L1L46L39R14R24R22L42R33L4L1R28R25L45R33L2L23L36L36R44R2R13L20R32L41R37L15L31L28L13L35L43L4R46L23L15R45L10R13R1R28L25L8L8L26R15L27L11L41L44R36R10R32L18R45R2L48L3R29R10R8R14R24R26L28L43R44R22R47R40R25R50R35R8R32R34R1R27R41R2L40L22L8L30L31L1L26L50L17L25R2L38R9L24R37R7R44L7R36L39R42R29R30L30R32L7L39L11R50R7L14R14R34L38R50L29R37R36R49R30R27R38L14L7L29L36R11L38L39L31L39L39R36R2R37R40L44R14L34R39R18L36R48R34R6R40L38L19R20L4R30R7L44R28L29R36L12L4R12R11R11R12L38L7R14R11R29R24R24L13R47R7R48L45L48L14L40R35L16L27R40R13L8L48L10L43R29R23L5R1L35L26R2R42R7L17L15R19L13L5L49L47L30R49L1L23L24L33L13R40R43R22R18R40L43R14R34L19L26R5L38R28L8L14R4L12R23L22R1L39L22R50R17R2L20L15R36L41L2L37L8L37L13R20R18L23R39L28R9L15R26L40R10L41R11R34L19R29R29L15R2R40R46R31R20L50R12R2L2R28R50R32L28R50L32L40R1R27L17L47L32R16R11R38R37R44R9L17L35L41L25L35L19R13L11R8R20R5R46L48L47R22L16R45R33L25R3L28L23L15L7L45R42R46R29L18R15R36L45L39L20L28L7L6L38L50R30L25L43L41R7R42R35R27R27R40R34R28L31R43R17L34L6R20R15R38L1R18L46L28L49L40R17R10L30R21L6R41R10L8R30L27R32R41R27L28R6L10R48R8L38L3L20L14R38R49R27R29R40L21L22R19L2R22R9R5L27L50L25L24L25L42L10R14L41L1R23R34R43R15L20R14L37R46R24L30R36R16L24R4L28L45L28L33R25L47L1L15R41R6L2L1R3L45L22R50L15L27R19R13R34L46L7R31L28R3R30L23L33L47L13L10L11L42L3L24L18L1L48R9R25R23L16L25R19L13R11R39R2R22L28R7R33L43L19R30L40R34R26L40L14R10L6L33L4L13L14R39R15R24R18R34R43L46R46L34L10L26R33L33R25L15R5L49L15L31L31R22R6R23L15R26L34L27L29L35L6L32R42L42L12R49R47L23R48L40R7R12R43R15L20L16L7L35L47R46R48L14L48R35R32R42R17R42R44L47L1L2L33R36L36L8R37R5L19R30L12R50R9L2L3L46L7L15R5R14L43R25R37L36R42R44R41R18L21R36L35L35R14L8L10R23R21R20L5R30L5R16L21L34R19L37L36R7R32L21R11R37L48L43L17L48L44L22L23R26R15R24L40R18L34L40R26L22L23R34L16L49R11R5L36L6R38R33R16L18R30R15R16R13L9R2R23R49R5R47R50L30L13R48R49L1R12L36R1L9L10L10L31R17L46R46R11L35R43L45R9R49R8L16R28R13L10L37L10R23R9R24L4R46L5L29L42L38L3R34R17L4L36L44R47L16"
else:
    position = (9, 1)
    sideLength = 4
    inputDirections = "10R5L5R10L4R5L5"
currentDirection = "R"

inputFile.pop()
inputFile.pop()

directions = queue.Queue()
cacheDistance = ""
for char in inputDirections:
    if char not in ["R", "L"]:
        cacheDistance += char
    else:
        directions.put(int(cacheDistance))
        directions.put(char)
        cacheDistance = ""
directions.put(int(cacheDistance))

validPositions = {}
for y in range(0, len(inputFile)):
    for x in range(0, len(inputFile[y])):
        if inputFile[y][x] in [".", "#"]:
            goodPosition = inputFile[y][x]
            validPositions[(x + 1, y + 1)] = goodPosition

def moveTest():
    global position
    global currentDirection
    tryPosition = []

    if currentDirection == "D":
        tryPosition = (position[0], position[1] + 1)
    elif currentDirection == "U":
        tryPosition = (position[0], position[1] - 1)
    elif currentDirection == "R":
        tryPosition = (position[0] + 1, position[1])
    elif currentDirection == "L":
        tryPosition = (position[0] - 1, position[1])

    if tryPosition in validPositions.keys():
        if validPositions[tryPosition] == ".":
            return [tryPosition, False]
        elif validPositions[tryPosition] == "#":
            return [position, True]
    else:
        if currentDirection == "D":
            if tryPosition[0] in list(range(1, 9)) or tryPosition[0] in list(range(13, 17)):
                if validPositions[(tryPosition[0], tryPosition[1] - 4)] == ".":
                    return [(tryPosition[0], tryPosition[1] - 4), False]
                elif validPositions[(tryPosition[0], tryPosition[1] - 4)] == "#":
                    return [position, True]
            
            elif tryPosition[0] in list(range(9, 13)):
                if validPositions[(tryPosition[0], tryPosition[1] - 12)] == ".":
                    return [(tryPosition[0], tryPosition[1] - 12), False]
                elif validPositions[(tryPosition[0], tryPosition[1] - 12)] == "#":
                    return [position, True]

        elif currentDirection == "U":
            if tryPosition[0] in list(range(1, 9)) or tryPosition[0] in list(range(13, 17)):
                if validPositions[(tryPosition[0], tryPosition[1] + 4)] == ".":
                    return [(tryPosition[0], tryPosition[1] + 4), False]
                elif validPositions[(tryPosition[0], tryPosition[1] + 4)] == "#":
                    return [position, True]

            elif tryPosition[0] in list(range(9, 13)):
                if validPositions[(tryPosition[0], tryPosition[1] + 12)] == ".":
                    return [(tryPosition[0], tryPosition[1] + 12), False]
                elif validPositions[(tryPosition[0], tryPosition[1] + 12)] == "#":
                    return [position, True]

        elif currentDirection == "R":
            if tryPosition[1] in list(range(1, 5)):
                if validPositions[(tryPosition[0] - 4, tryPosition[1])] == ".":
                    return [(tryPosition[0] - 4, tryPosition[1]), False]
                elif validPositions[(tryPosition[0] - 4, tryPosition[1])] == "#":
                    return [position, True]

            elif tryPosition[1] in list(range(5, 9)):
                if validPositions[(tryPosition[0] - 12, tryPosition[1])] == ".":
                    return [(tryPosition[0] - 12, tryPosition[1]), False]
                elif validPositions[(tryPosition[0] - 12, tryPosition[1])] == "#":
                    return [position, True]

            elif tryPosition[1] in list(range(9, 13)):
                if validPositions[(tryPosition[0] - 8, tryPosition[1])] == ".":
                    return [(tryPosition[0] - 8, tryPosition[1]), False]
                elif validPositions[(tryPosition[0] - 8, tryPosition[1])] == "#":
                    return [position, True]

        elif currentDirection == "L":
            if tryPosition[1] in list(range(1, 5)):
                if validPositions[(tryPosition[0] + 4, tryPosition[1])] == ".":
                    return [(tryPosition[0] + 4, tryPosition[1]), False]
                elif validPositions[(tryPosition[0] + 4, tryPosition[1])] == "#":
                    return [position, True]

            elif tryPosition[1] in list(range(5, 9)):
                if validPositions[(tryPosition[0] + 12, tryPosition[1])] == ".":
                    return [(tryPosition[0] + 12, tryPosition[1]), False]
                elif validPositions[(tryPosition[0] + 12, tryPosition[1])] == "#":
                    return [position, True]

            elif tryPosition[1] in list(range(9, 13)):
                if validPositions[(tryPosition[0] + 8, tryPosition[1])] == ".":
                    return [(tryPosition[0] + 8, tryPosition[1]), False]
                elif validPositions[(tryPosition[0] + 8, tryPosition[1])] == "#":
                    return [position, True]

def moveReal():
    global position
    global currentDirection
    tryPosition = []

    if currentDirection == "D":
        tryPosition = (position[0], position[1] + 1)
    elif currentDirection == "U":
        tryPosition = (position[0], position[1] - 1)
    elif currentDirection == "R":
        tryPosition = (position[0] + 1, position[1])
    elif currentDirection == "L":
        tryPosition = (position[0] - 1, position[1])

    if tryPosition in validPositions.keys():
        if validPositions[tryPosition] == ".":
            return [tryPosition, False]
        elif validPositions[tryPosition] == "#":
            return [position, True]
    else:
        if currentDirection == "D":
            if tryPosition[0] in list(range(1, 51)):
                if validPositions[(tryPosition[0], tryPosition[1] - 100)] == ".":
                    return [(tryPosition[0], tryPosition[1] - 100), False]
                elif validPositions[(tryPosition[0], tryPosition[1] - 100)] == "#":
                    return [position, True]
            
            elif tryPosition[0] in list(range(51, 101)):
                if validPositions[(tryPosition[0], tryPosition[1] - 150)] == ".":
                    return [(tryPosition[0], tryPosition[1] - 150), False]
                elif validPositions[(tryPosition[0], tryPosition[1] - 150)] == "#":
                    return [position, True]

            elif tryPosition[0] in list(range(101, 151)):
                if validPositions[(tryPosition[0], tryPosition[1] - 50)] == ".":
                    return [(tryPosition[0], tryPosition[1] - 50), False]
                elif validPositions[(tryPosition[0], tryPosition[1] - 50)] == "#":
                    return [position, True]

        elif currentDirection == "U":
            if tryPosition[0] in list(range(1, 51)):
                if validPositions[(tryPosition[0], tryPosition[1] + 100)] == ".":
                    return [(tryPosition[0], tryPosition[1] + 100), False]
                elif validPositions[(tryPosition[0], tryPosition[1] + 100)] == "#":
                    return [position, True]
            
            elif tryPosition[0] in list(range(51, 101)):
                if validPositions[(tryPosition[0], tryPosition[1] + 150)] == ".":
                    return [(tryPosition[0], tryPosition[1] + 150), False]
                elif validPositions[(tryPosition[0], tryPosition[1] + 150)] == "#":
                    return [position, True]

            elif tryPosition[0] in list(range(101, 151)):
                if validPositions[(tryPosition[0], tryPosition[1] + 50)] == ".":
                    return [(tryPosition[0], tryPosition[1] + 50), False]
                elif validPositions[(tryPosition[0], tryPosition[1] + 50)] == "#":
                    return [position, True]

        elif currentDirection == "R":
            if tryPosition[1] in list(range(1, 51)) or tryPosition[1] in list(range(101, 151)):
                if validPositions[(tryPosition[0] - 100, tryPosition[1])] == ".":
                    return [(tryPosition[0] - 100, tryPosition[1]), False]
                elif validPositions[(tryPosition[0] - 100, tryPosition[1])] == "#":
                    return [position, True]

            elif tryPosition[1] in list(range(51, 101)) or list(range(151, 201)):
                if validPositions[(tryPosition[0] - 50, tryPosition[1])] == ".":
                    return [(tryPosition[0] - 50, tryPosition[1]), False]
                elif validPositions[(tryPosition[0] - 50, tryPosition[1])] == "#":
                    return [position, True]

        elif currentDirection == "L":
            if tryPosition[1] in list(range(1, 51)) or tryPosition[1] in list(range(101, 151)):
                if validPositions[(tryPosition[0] + 100, tryPosition[1])] == ".":
                    return [(tryPosition[0] + 100, tryPosition[1]), False]
                elif validPositions[(tryPosition[0] + 100, tryPosition[1])] == "#":
                    return [position, True]

            elif tryPosition[1] in list(range(51, 101)) or list(range(151, 201)):
                if validPositions[(tryPosition[0] + 50, tryPosition[1])] == ".":
                    return [(tryPosition[0] + 50, tryPosition[1]), False]
                elif validPositions[(tryPosition[0] + 50, tryPosition[1])] == "#":
                    return [position, True]

def turn(turnDirection):
    global currentDirection
    directionList = ["U", "R", "D", "L"]
    currentDirectionIndex = directionList.index(currentDirection)

    if turnDirection == "R":
        currentDirection = directionList[(currentDirectionIndex + 1) % 4]
    elif turnDirection == "L":
        currentDirection = directionList[(currentDirectionIndex - 1) % 4]

while not directions.empty():
    currentInstruction = directions.get()

    if currentInstruction == "R":
        turn("R")
    elif currentInstruction == "L":
        turn("L")
    else:
        for _ in range(currentInstruction):
            if fileName == "AOC22test.txt)": pp = moveTest()
            else: pp = moveReal()
            if pp[1]:
                continue
            position = pp[0]
            # print(position)
            # print(currentDirection)
        
print(position)
print(currentDirection)
facing = ["R", "D", "L", "U"]
answer = (position[1] * 1000) + (position[0] * 4) + facing.index(currentDirection)
print(answer)