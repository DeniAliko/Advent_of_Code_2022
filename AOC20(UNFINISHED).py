file = open("AOC20test.txt")
inputFile = []
outputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(int(format(i.strip())))
    outputFile.append(int(format(i.strip())))

def swap(list, index1, index2):
    index1Item = list[index1]
    index2Item = list[index2]

    list.pop(index1)
    list.insert(index2, index1Item)
    if index1 < index2:
        list.pop(index2 - 1)
    else:
        list.pop(index2 + 1)
    list.insert(index1, index2Item)

for i in inputFile:
    if i > 0:
        for _ in range(i):
            swap(outputFile, outputFile.index(i), outputFile.index(i) + 1 % len(outputFile) - 1)
    elif i < 0:
        for _ in range(-i):
            swap(outputFile, outputFile.index(i) - 1 % len(outputFile) - 1, outputFile.index(i))

print(outputFile)