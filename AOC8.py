file = open("AOC8.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

def visibilityCheck(x, y):
    score = 0
    # from bottom to point of interest
    for i in range(0, y):
        if int(inputFile[y][x]) <= int(inputFile[i][x]):
            score += 1
            break
    
    # from POI to top
    for i in range(y + 1, len(inputFile)):
        if int(inputFile[y][x]) <= int(inputFile[i][x]):
            score += 1
            break

    # from left to POI
    for i in range(0, x):
        if int(inputFile[y][x]) <= int(inputFile[y][i]):
            score += 1
            break

    # from POI to right
    for i in range(x + 1, len(inputFile[y])):
        if int(inputFile[y][x]) <= int(inputFile[y][i]):
            score += 1
            break

    if score < 4:
        return True
    else:
        return False

count = 0
for i in range(0, len(inputFile)):
    for j in range(0, len(inputFile[i])):
        if visibilityCheck(i, j):
            count += 1

print(count)

def getScenicScore(x, y):
    scenicScore = 0
    directionalScore = 0

    # X right
    for i in range(x + 1, len(inputFile[y])):
        directionalScore += 1
        if int(inputFile[y][i]) >= int(inputFile[y][x]):
            break
    dScore1 = directionalScore
    directionalScore = 0

    # Y down
    for i in range(y + 1, len(inputFile)):
        directionalScore += 1
        if int(inputFile[i][x]) >= int(inputFile[y][x]):
            break
    dScore2 = directionalScore
    directionalScore = 0

    # X left
    for i in range(x - 1, -1, -1):
        directionalScore += 1
        if int(inputFile[y][i]) >= int(inputFile[y][x]):
            break
    dScore3 = directionalScore
    directionalScore = 0

    # Y up
    for i in range(y - 1, -1, -1):
        directionalScore += 1
        if int(inputFile[i][x]) >= int(inputFile[y][x]):
            break
    dScore4 = directionalScore
    directionalScore = 0

    return dScore1 * dScore2 * dScore3 * dScore4

scenicScores = []
for i in range(0, len(inputFile)):
    for j in range(0, len(inputFile[i])):
        scenicScores.append([getScenicScore(i, j), (i, j)])

print(scenicScores)
print(max(scenicScores))