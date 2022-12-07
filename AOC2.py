file = open("AOC2.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

#print(inputFile)

score = 0

# Column 2 is what you choose:
for item in inputFile:
    if item[2] == "X":
        score += 1

        if item[0] == "A":
            score += 3
        elif item[0] == "B":
            score += 0
        elif item[0] == "C":
            score += 6
    elif item[2] == "Y":
        score += 2

        if item[0] == "A":
            score += 6
        elif item[0] == "B":
            score += 3
        elif item[0] == "C":
            score += 0
    elif item[2] == "Z":
        score += 3

        if item[0] == "A":
            score += 0
        elif item[0] == "B":
            score += 6
        elif item[0] == "C":
            score += 3

print(score)
score = 0

# Column 2 is how the game ends:
for item in inputFile:
    if item[2] == "X":
        score += 0

        if item[0] == "A":
            score += 3
        elif item[0] == "B":
            score += 1
        elif item[0] == "C":
            score += 2
    elif item[2] == "Y":
        score += 3

        if item[0] == "A":
            score += 1
        elif item[0] == "B":
            score += 2
        elif item[0] == "C":
            score += 3
    elif item[2] == "Z":
        score += 6

        if item[0] == "A":
            score += 2
        elif item[0] == "B":
            score += 3
        elif item[0] == "C":
            score += 1

print(score)
