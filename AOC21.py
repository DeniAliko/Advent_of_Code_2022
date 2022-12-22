file = open("AOC21.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

dictLines = {}
for line in inputFile:
    try: 
        dictLines[line.split(" ")[0].strip(":")] = int(line.split(" ")[1])
    except ValueError:
        dictLines[line.split(" ")[0].strip(":")] = line.split(" ")[1:4]

def getNumber(monkey):
    if isinstance(dictLines[monkey], int):
        return dictLines[monkey]
    else:
        if dictLines[monkey][1] == "+":
            return getNumber(dictLines[monkey][0]) + getNumber(dictLines[monkey][2])
        elif dictLines[monkey][1] == "-":
            return getNumber(dictLines[monkey][0]) - getNumber(dictLines[monkey][2])
        elif dictLines[monkey][1] == "*":
            return getNumber(dictLines[monkey][0]) * getNumber(dictLines[monkey][2])
        elif dictLines[monkey][1] == "/":
            return getNumber(dictLines[monkey][0]) / getNumber(dictLines[monkey][2])

print("Part 1:", getNumber("root"))

operations = []
def getChildrenOperations(monkey):

    # Check if it is an integer:
    if isinstance(dictLines[monkey], int):
        return None

    compare1 = getNumber(dictLines[monkey][0])
    dictLines["humn"] += 1
    compare2 = getNumber(dictLines[monkey][0])
    dictLines["humn"] -= 1

    if compare1 == compare2:
        knownValue = getNumber(dictLines[monkey][0])
        print(dictLines[monkey][0] + " is known (first one)")

        operations.append([knownValue, dictLines[monkey][1]])
        getChildrenOperations(dictLines[monkey][2])

    else:
        knownValue = getNumber(dictLines[monkey][2])
        print(dictLines[monkey][2] + " is known (second one)")

        operations.append([dictLines[monkey][1], knownValue])
        getChildrenOperations(dictLines[monkey][0])

# Find which half humn is in
compare1 = getNumber(dictLines["root"][0])
dictLines["humn"] += 1
compare2 = getNumber(dictLines["root"][0])
dictLines["humn"] -= 1
if compare1 == compare2:
    eqSol = getNumber(dictLines["root"][0])
    print(dictLines["root"][0] + " is known (first one)")
    getChildrenOperations(dictLines["root"][2])
else:
    eqSol = getNumber(dictLines["root"][2])
    print(dictLines["root"][2] + " is known (second one)")
    getChildrenOperations(dictLines["root"][0])

print(eqSol)
print(operations)

humnSays = eqSol
for operation in operations:
    if operation[0] == "+":
        humnSays -= operation[1]
    elif operation[1] == "+":
        humnSays -= operation[0]
    elif operation[0] == "*":
        humnSays /= operation[1]
    elif operation[1] == "*":
        humnSays /= operation[0]
    elif operation[0] == "-":
        humnSays += operation[1]
    elif operation[1] == "-":
        humnSays -= operation[0]
        humnSays *= -1
    elif operation[0] == "/":
        humnSays *= operation[1]

print(humnSays)