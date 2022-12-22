file = open("AOC20test.txt")
inputFile = []
outputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(int(format(i.strip())))
    outputFile.append(int(format(i.strip())))

def goLeft(list, index):
    item = list[index]
    if index == 0:
        list.pop(index)
        list.insert(index - 1, item)
    elif index == 1:
        list.pop(index)
        list.insert(len(list), item)
    else:
        list.pop(index)
        list.insert(index - 1, item)

def goRight(list, index):
    item = list[index]
    if index == len(list) - 1:
        list.pop(index)
        list.insert(1, item)
    else:
        list.pop(index)
        list.insert(index + 1, item)