file = open("AOC10.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

registry = 1
cycle = 1
checkCycles = [20, 60, 100, 140, 180, 220]
signalStrengths = []

def cycleCheck():
    global cycle
    global registry
    if cycle in checkCycles:
        signalStrengths.append([cycle, registry, cycle*registry])

for i in inputFile:
    if i == "noop":
        cycleCheck()
        cycle += 1
    else:
        cycleCheck()
        cycle += 1
        cycleCheck()
        cycle += 1
        registry += int(i.split(" ")[1])

print(signalStrengths)
part1Answer = 0
for i in signalStrengths:
    part1Answer += i[2]
print(part1Answer)

# oh boy here comes part 2

line = ""
registry = 1
cycle = 1

def drawPixel():
    global line
    global registry
    global cycle

    spritePos = [registry, registry + 1, registry + 2]

    if len(line) == 40:
        print(line)
        line = ""
    if len(line) + 1 in spritePos:
        line += "#"
    else:
        line += "."

for i in inputFile:
    if i == "noop":
        drawPixel()
        cycle += 1
    else:
        drawPixel()
        cycle += 1
        drawPixel()
        registry += int(i.split(" ")[1])
        cycle += 1
print(line)