import math

file = open("AOC25.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

maxLength = 0
for line in inputFile:
    if len(line) > maxLength:
        maxLength = len(line)

organizedList = []
for line in inputFile:
    cacheList = []
    for char in line:
        cacheList.append(char)
    cacheList.reverse()
    for _ in range(maxLength - len(cacheList)):
        cacheList.append("0")
    organizedList.append(cacheList)
    cacheList = []

# Every SNAFU number is a list from ones place upwards

for number in organizedList:
    for digitIndex in range(0, len(number)):
        if number[digitIndex] == "-":
            number[digitIndex] = -1
        elif number[digitIndex] == "=":
            number[digitIndex] = -2
        else:
            number[digitIndex] = int(number[digitIndex])

decimalRepresentations = []
for number in organizedList:
    cacheSum = 0
    for i in range(0, len(number)):
        cacheSum += number[i] * (5**i)
    decimalRepresentations.append(cacheSum)

decimalSum = sum(decimalRepresentations)
print("Sum in base 10:", decimalSum)

anotherDecimalSum = decimalSum
base5SumList = []
done = False
while not done:
    remainder = decimalSum % 5
    quotient = (decimalSum - (remainder)) / 5
    base5SumList.append(int(remainder))
    if remainder == decimalSum:
        done = True
        break
    decimalSum = quotient

# print(base5SumList)
SNAFUdiff = 0
for pp in range(0, len(base5SumList)):
    SNAFUdiff += 2 * 5**pp
# print(SNAFUdiff)

tempSum = anotherDecimalSum + SNAFUdiff

answer = []
done = False
while not done:
    remainder = tempSum % 5
    quotient = (tempSum - (remainder)) / 5
    answer.append(int(remainder) - 2)
    if remainder == tempSum:
        done = True
        break
    tempSum = quotient
answer.reverse()

realAnswer = ""
for char in answer:
    if char == -1:
        realAnswer += "-"
    elif char == -2:
        realAnswer += "="
    else:
        realAnswer += str(char)

print("Answer:", realAnswer)