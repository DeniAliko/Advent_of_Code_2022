file = open("AOC6.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

inputString = ""
for i in inputFile:
    inputString += i

testCase = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
for i in range(3, len(inputString)):
    if inputString[i] != inputString[i-1] and inputString[i] != inputString[i-2] and inputString[i] != inputString[i-3] and inputString[i-1] != inputString[i-2] and inputString[i-1] != inputString[i-3] and inputString[i-2] != inputString[i-3]:
        break
    else:
        print(i+2)

#for i in range(3, len(testCase)):
#    if testCase[i] != testCase[i-1] and testCase[i] != testCase[i-2] and testCase[i] != testCase[i-3] and testCase[i-1] != testCase[i-2] and testCase[i-1] != testCase[i-3] and testCase[i-2] != testCase[i-3]:
#        break
#    else:
#        print(i+2)

# part 2
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def letterCheck(a, b, c, d, e, f, g, h, i, j, k, l, m, n):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    letterCheckList = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]
    for i in letterCheckList:
        if i in letters:
            letters.remove(i)
        else:
            return False
    if len(letters) == 12:
        return True
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in range(13, len(inputString)):
    if letterCheck(inputString[i], inputString[i-1], inputString[i-2], inputString[i-3], inputString[i-4], inputString[i-5], inputString[i-6], inputString[i-7], inputString[i-8], inputString[i-9], inputString[i-10], inputString[i-11], inputString[i-12], inputString[i-13]):
        print(i+1)
        break

testCase = "bvwbjplbgvbhsrlpgdmjqwftvncz"
#for i in range(13, len(testCase)):
#    if letterCheck(testCase[i], testCase[i-1], testCase[i-2], testCase[i-3], testCase[i-4], testCase[i-5], testCase[i-6], testCase[i-7], testCase[i-8], testCase[i-9], testCase[i-10], testCase[i-11], testCase[i-12], testCase[i-13]):
#        print(i+1)
#        break
