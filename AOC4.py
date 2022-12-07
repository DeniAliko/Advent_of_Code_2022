file = open("AOC4.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

testLine = "7-50,8-33"

split1 = testLine.split(",")
#print(split1)
organizedList = []
cacheArray = []
for item in split1:
    cacheArray.append(item.split("-"))
    #print(item.split("-"))
    organizedList.append(cacheArray)
    cacheArray = []

#print(organizedList)

split1 = []
for item in inputFile:
    split1.append(item.split(","))

#print(split1)

organizedList = []
cacheArray = []
for item in split1:
    cacheArray.append(item[0].split("-") + item[1].split("-"))
    #print(item[0].split("-"))
    organizedList.append(cacheArray)
    cacheArray = []

#print(organizedList)

count = 0
for item in organizedList:
    if int(item[0][0]) >= int(item[0][2]) and int(item[0][1]) <= int(item[0][3]):
        count += 1
    elif int(item[0][0]) <= int(item[0][2]) and int(item[0][1]) >= int(item[0][3]):
        count +=1

print(len(organizedList))
print(count, "Part 1")

# Part 2
count = 0
for item in organizedList:
    #full overlap:
    if int(item[0][0]) >= int(item[0][2]) and int(item[0][1]) <= int(item[0][3]):
        count += 1
    elif int(item[0][0]) <= int(item[0][2]) and int(item[0][1]) >= int(item[0][3]):
        count +=1
    # 1 2 1 2 and 2 1 2 1
    elif int(item[0][0]) <= int(item[0][2]) and int(item[0][1]) >= int(item[0][2]):
        count += 1
    elif int(item[0][2]) <= int(item[0][0]) and int(item[0][3]) >= int(item[0][0]):
        count +=1
print(count, "Part 2")
