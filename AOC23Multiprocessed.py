from multiprocessing import Pool
import time

start = time.time()

file = open("AOC23test.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

inputFile.reverse()

elfCount = 0
startingPositions = []
for i in range(0, len(inputFile)):
    for j in range(0, len(inputFile[i])):
        if inputFile[i][j] == "#":
            startingPositions.append([[j + 1, i + 1], [j + 1, i + 1]])
            elfCount += 1

currentPositions = list(startingPositions)
proposedMoves = []
movementQueue = ["N", "S", "W", "E"]

def proposeElf(coords):
    foundMove = False

    neighbors = []
    for delX in [-1, 0, 1]:
        if delX == 0:
            for delY in [1, -1]:
                if [coords[0] + delX, coords[1] + delY] in currentPositions:
                    neighbors.append(False)
                else:
                    neighbors.append(True)
        else:
            for delY in [1, 0, -1]:
                if [coords[0] + delX, coords[1] + delY] in currentPositions:
                    neighbors.append(False)
                else:
                    neighbors.append(True)

    # 0 3 5
    # 1   6
    # 2 4 7
    # True if accessible

    if neighbors[0] and neighbors[1] and neighbors[2] and neighbors[3] and neighbors[4] and neighbors[5] and neighbors[6] and neighbors[7]:
        proposed = coords
        proposedMoves.append(proposed)
        foundMove = True

    else:
        for direction in movementQueue:
            if direction == "N":
                if neighbors[0] and neighbors[3] and neighbors[5]:
                    proposed = [coords[0], coords[1] + 1]
                    proposedMoves.append(proposed)
                    foundMove = True

                    break

            elif direction == "S":
                if neighbors[2] and neighbors[4] and neighbors[7]:
                    proposed = [coords[0], coords[1] - 1]
                    proposedMoves.append(proposed)
                    foundMove = True

                    break

            elif direction == "W":
                if neighbors[0] and neighbors[1] and neighbors[2]:
                    proposed = [coords[0] - 1, coords[1]]
                    proposedMoves.append(proposed)
                    foundMove = True

                    break

            elif direction == "E":
                if neighbors[5] and neighbors[6] and neighbors[7]:
                    proposed = [coords[0] + 1, coords[1]]
                    proposedMoves.append(proposed)
                    foundMove = True
                    
                    break

    if not foundMove:
        proposed = coords
    proposedMoves.append(proposed)

    return proposed

for elf in currentPositions:
    elf[1] = proposeElf(elf[0])
    print(elf[1])

checkedMove = movementQueue[0]
movementQueue.pop(0)
movementQueue.append(checkedMove)

print(currentPositions)
print(proposedMoves)