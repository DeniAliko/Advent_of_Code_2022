from multiprocessing import Pool
import time

start = time.time()

file = open("AOC23.txt")
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
            startingPositions.append([j + 1, i + 1])
            elfCount += 1

currentPositions = list(startingPositions)
proposedMoves = []
elves = []

class Elf:
    def __init__(self, position, movementQueue, proposed):
        self.position = position
        self.movementQueue = movementQueue
        self.proposed = proposed

    def proposeMove(self):
        foundMove = False

        neighbors = []
        for delX in [-1, 0, 1]:
            if delX == 0:
                for delY in [1, -1]:
                    if [self.position[0] + delX, self.position[1] + delY] in currentPositions:
                        neighbors.append(False)
                    else:
                        neighbors.append(True)
            else:
                for delY in [1, 0, -1]:
                    if [self.position[0] + delX, self.position[1] + delY] in currentPositions:
                        neighbors.append(False)
                    else:
                        neighbors.append(True)

        # 0 3 5
        # 1   6
        # 2 4 7
        # True if accessible

        if neighbors[0] and neighbors[1] and neighbors[2] and neighbors[3] and neighbors[4] and neighbors[5] and neighbors[6] and neighbors[7]:
            self.proposed = [self.position[0], self.position[1]]
            proposedMoves.append(self.proposed)
            foundMove = True

            firstCheck = self.movementQueue[0]
            self.movementQueue.pop(0)
            self.movementQueue.append(firstCheck)

            return
        for direction in self.movementQueue:
            if direction == "N":
                if neighbors[0] and neighbors[3] and neighbors[5]:
                    self.proposed = [self.position[0], self.position[1] + 1]
                    proposedMoves.append(self.proposed)
                    foundMove = True

                    break

            elif direction == "S":
                if neighbors[2] and neighbors[4] and neighbors[7]:
                    self.proposed = [self.position[0], self.position[1] - 1]
                    proposedMoves.append(self.proposed)
                    foundMove = True

                    break

            elif direction == "W":
                if neighbors[0] and neighbors[1] and neighbors[2]:
                    self.proposed = [self.position[0] - 1, self.position[1]]
                    proposedMoves.append(self.proposed)
                    foundMove = True
 
                    break

            elif direction == "E":
                if neighbors[5] and neighbors[6] and neighbors[7]:
                    self.proposed = [self.position[0] + 1, self.position[1]]
                    proposedMoves.append(self.proposed)
                    foundMove = True
                    
                    break

        if not foundMove:
            self.proposed = self.position
        firstCheck = self.movementQueue[0]
        self.movementQueue.pop(0)
        self.movementQueue.append(firstCheck)

    def move(self):
        if proposedMoves.count(self.proposed) == 1:
            self.position = self.proposed

# test = Elf([1, 1], ["N", "S", "W", "E"], [0, 0])

for startingPos in startingPositions:
    elves.append(Elf(startingPos, ["N", "S", "W", "E"], [0, 0]))

previousPositions = []
roundCount = 0
done = False

print("Start:")
print(startingPositions)
# One round:
while done == False:
# for _ in range(10):
    proposedMoves = []
    # with Pool(8) as p:
    #     p.imap_unordered(Elf.proposeMove, elves)
    for elf in elves:
        elf.proposeMove()

    previousPositions = list(currentPositions)
    currentPositions = []
    for elf in elves:
        currentPositions.append(elf.position)
        # print(elf.movementQueue, elf.position)

    for elf in elves:
        elf.move()

    currentPositions = []
    for elf in elves:
        currentPositions.append(elf.position)

    roundCount += 1
    if previousPositions == currentPositions:
        done == True
        print(roundCount)
        break
        

    print("Round:", roundCount)
    # print(currentPositions)

yMax = 0
yMin = 10000000000
xMax = 0
xMin = 10000000000
for coord in currentPositions:
    if coord[0] > xMax:
        xMax = coord[0]
    if coord[0] < xMin:
        xMin = coord[0]
    if coord[1] > yMax:
        yMax = coord[1]
    if coord[1] < yMin:
        yMin = coord[1]

print("X:", xMax, xMin)
print("Y:", yMax, yMin)
print("Free space:", (yMax - (yMin - 1)) * (xMax - (xMin - 1)) - len(startingPositions))
print("Rounds until done:", roundCount)

end = time.time()
print("Time:", end-start)