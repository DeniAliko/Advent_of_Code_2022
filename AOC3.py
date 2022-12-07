file = open("AOC3.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# Part 1
organizedList = []
cacheList = []
for i in inputFile:
    cacheCompartment = ""
    for j in range(0, int(len(i)/2)):
        cacheCompartment += i[j]
    cacheList.append(cacheCompartment)
    cacheCompartment = ""
    for j in range(int(len(i)/2), len(i)):
        cacheCompartment += i[j]
    cacheList.append(cacheCompartment)
    organizedList.append(cacheList)
    cacheList = []

#print(organizedList)
lengthCount = 0
priorityScore = 0
for i in organizedList:
    for j in range(0, len(i[0])):
        if i[0][j] in i[1]:
            if i[0][j] in lowercase:
                priorityScore += lowercase.index(i[0][j])+1
                lengthCount += 1
                #print("A lowercase")
                break
            elif i[0][j] in uppercase:
                priorityScore += uppercase.index(i[0][j])+27
                lengthCount += 1
                #print("A uppercase")
                break
            break

print(priorityScore)
#print(len(organizedList))
#print(lengthCount)

# Part 2
organizedList = []
cacheList = []
thisonerandomcounter = 0
for i in inputFile:
    if thisonerandomcounter < 3:
        cacheList.append(i)
        thisonerandomcounter += 1
    if thisonerandomcounter == 3:
        organizedList.append(cacheList)
        cacheList = []
        thisonerandomcounter = 0

print(len(organizedList))
for i in organizedList:
    if len(i) != 3:
        print("doodoofard")


testlist = [["vJrwpWtwJgWrhcsFMMfFFhFp","jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL","PmmdzqPrVvPwwTWBwg"],["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn","ttgJtRGJQctTZtZT","CrZsJsPPZsGzwwsLwLmpwMDw"]]

priorityScore = 0
letters = lowercase + uppercase
for i in organizedList:
    for letter in letters:
        if letter in i[0] and letter in i[1] and letter in i[2]:
            priorityScore += letters.index(letter)+1

print(priorityScore)
