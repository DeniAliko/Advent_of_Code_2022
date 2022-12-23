import ast

file = open("AOC13.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

organizedList = []
cacheList = []
for i in inputFile:
    if i != "":
        cacheList.append(i)
    else:
        organizedList.append(cacheList)
        cacheList = []
organizedList.append(cacheList)
cacheList = []
organizederList = []
for pair in organizedList:
    cacheList = [ast.literal_eval(pair[0]), ast.literal_eval(pair[1])]
    organizederList.append(cacheList)
    cacheList = []

def compare(list1, list2):
    currentIndex = 0

    if list1 == list2:
        return "inconclusive"

    while True:

        if currentIndex + 1 > len(list1) and currentIndex + 1 <= len(list2):
            return True
        elif currentIndex + 1 > len(list2) and currentIndex + 1 <= len(list1):
            return False

        if isinstance(list1[currentIndex], int) and isinstance(list2[currentIndex], int):
            if int(list1[currentIndex]) > int(list2[currentIndex]):
                return False
            elif int(list1[currentIndex]) < int(list2[currentIndex]):
                return True
            elif int(list1[currentIndex]) == int(list2[currentIndex]):
                currentIndex += 1
                continue
        elif isinstance(list1[currentIndex], list) and isinstance(list2[currentIndex], list):
            if compare(list1[currentIndex], list2[currentIndex]) != "inconclusive":
                return compare(list1[currentIndex], list2[currentIndex])
            else:
                currentIndex += 1
                continue
        elif isinstance(list1[currentIndex], list) and isinstance(list2[currentIndex], int):
            if compare(list1[currentIndex], [list2[currentIndex]]) != "inconclusive":
                return compare(list1[currentIndex], [list2[currentIndex]])
            else:
                currentIndex += 1
                continue
        elif isinstance(list1[currentIndex], int) and isinstance(list2[currentIndex], list):
            if compare([list1[currentIndex]], list2[currentIndex]) != "inconclusive":
                return compare([list1[currentIndex]], list2[currentIndex])
            else:
                currentIndex += 1
                continue

goodIndexes = []
for pairIndex in range(0, len(organizederList)):
    if compare(organizederList[pairIndex][0], organizederList[pairIndex][1]) == True:
        goodIndexes.append(pairIndex + 1)

print(sum(goodIndexes))

# parte dos

organizedList = []
for line in inputFile:
    if line != "":
        organizedList.append(ast.literal_eval(line))

organizedList.append([[2]])
organizedList.append([[6]])

# print(organizedList)

reverseOrder = [organizedList[0]]
organizedList.pop(0)

for packet in organizedList:
    for index in range(0, len(reverseOrder)):
        if index == 0:
            if compare(packet, reverseOrder[index]) == False:
                reverseOrder.insert(index, packet)
                break
        if index == len(reverseOrder) - 1:
            if compare(packet, reverseOrder[index]):
                reverseOrder.append(packet)
                break
        elif compare(reverseOrder[index], packet) == False and compare(packet, reverseOrder[index + 1]) == False:
            reverseOrder.insert(index + 1, packet)
            break

reverseOrder.reverse()
print(reverseOrder)

print((reverseOrder.index([[2]]) + 1) * (reverseOrder.index([[6]]) + 1))