import math

gate = input(": ")

monkey0 = [71, 56, 50, 73]
monkey1 = [70, 89, 82]
monkey2 = [52, 95]
monkey3 = [94, 64, 69, 87, 70]
monkey4 = [98, 72, 98, 53, 97, 51]
monkey5 = [79]
monkey6 = [77, 55, 63, 93, 66, 90, 88, 71]
monkey7 = [54, 97, 87, 70, 59, 82, 59]

work0 = 0
work1 = 0
work2 = 0
work3 = 0
work4 = 0
work5 = 0
work6 = 0
work7 = 0

lcm = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19

def worryOp(x, string):
    global gate
    if string[0] == "+":
        x += int(string.split(" ")[1])
    elif string[0] == "*" and string != "**":
        x *= int(string.split(" ")[1])
    else:
        x = x ** 2
    if gate == "1":
        return math.floor(x/3)
    if gate != "1":
        return x % lcm

def monkeySee0():
    removeIndecies = []
    removeWorries = []
    global work0
    for i in range(0, len(monkey0)):
        work0 += 1
        pp = worryOp(monkey0[i], "* 11")
        if pp % 13 == 0:
            removeIndecies.append(i)
            monkey1.append(pp)
        else:
            removeIndecies.append(i)
            monkey7.append(pp)
    for i in removeIndecies:
        removeWorries.append(monkey0[i])
    for i in removeWorries:
        monkey0.remove(i)

def monkeySee1():
    removeIndecies = []
    removeWorries = []
    global work1
    for i in range(0, len(monkey1)):
        work1 += 1
        pp = worryOp(monkey1[i], "+ 1")
        if pp % 7 == 0:
            removeIndecies.append(i)
            monkey3.append(pp)
        else:
            removeIndecies.append(i)
            monkey6.append(pp)
    for i in removeIndecies:
        removeWorries.append(monkey1[i])
    for i in removeWorries:
        monkey1.remove(i)

def monkeySee2():
    removeIndecies = []
    removeWorries = []
    global work2
    for i in range(0, len(monkey2)):
        work2 += 1
        pp = worryOp(monkey2[i], "**")
        if pp % 3 == 0:
            removeIndecies.append(i)
            monkey5.append(pp)
        else:
            removeIndecies.append(i)
            monkey4.append(pp)
    for i in removeIndecies:
        removeWorries.append(monkey2[i])
    for i in removeWorries:
        monkey2.remove(i)

def monkeySee3():
    removeIndecies = []
    removeWorries = []
    global work3
    for i in range(0, len(monkey3)):
        work3 += 1
        pp = worryOp(monkey3[i], "+ 2")
        if pp % 19 == 0:
            removeIndecies.append(i)
            monkey2.append(pp)
        else:
            removeIndecies.append(i)
            monkey6.append(pp)
    for i in removeIndecies:
        removeWorries.append(monkey3[i])
    for i in removeWorries:
        monkey3.remove(i)

def monkeySee4():
    removeIndecies = []
    removeWorries = []
    global work4
    for i in range(0, len(monkey4)):
        work4 += 1
        pp = worryOp(monkey4[i], "+ 6")
        if pp % 5 == 0:
            removeIndecies.append(i)
            monkey0.append(pp)
        else:
            removeIndecies.append(i)
            monkey5.append(pp)
    for i in removeIndecies:
        removeWorries.append(monkey4[i])
    for i in removeWorries:
        monkey4.remove(i)

def monkeySee5():
    removeIndecies = []
    removeWorries = []
    global work5
    for i in range(0, len(monkey5)):
        work5 += 1
        pp = worryOp(monkey5[i], "+ 7")
        if pp % 2 == 0:
            removeIndecies.append(i)
            monkey7.append(pp)
        else:
            removeIndecies.append(i)
            monkey0.append(pp)
    for i in removeIndecies:
        removeWorries.append(monkey5[i])
    for i in removeWorries:
        monkey5.remove(i)

def monkeySee6():
    removeIndecies = []
    removeWorries = []
    global work6
    for i in range(0, len(monkey6)):
        work6 += 1
        pp = worryOp(monkey6[i], "* 7")
        if pp % 11 == 0:
            removeIndecies.append(i)
            monkey2.append(pp)
        else:
            removeIndecies.append(i)
            monkey4.append(pp)
    for i in removeIndecies:
        removeWorries.append(monkey6[i])
    for i in removeWorries:
        monkey6.remove(i)

def monkeySee7():
    removeIndecies = []
    removeWorries = []
    global work7
    for i in range(0, len(monkey7)):
        work7 += 1
        pp = worryOp(monkey7[i], "+ 8")
        if pp % 17 == 0:
            removeIndecies.append(i)
            monkey1.append(pp)
        else:
            removeIndecies.append(i)
            monkey3.append(pp)
    for i in removeIndecies:
        removeWorries.append(monkey7[i])
    for i in removeWorries:
        monkey7.remove(i)

if gate == "1":
    rounds = 20
else:
    rounds = 10000

for i in range(rounds):
    monkeySee0()
    monkeySee1()
    monkeySee2()
    monkeySee3()
    monkeySee4()
    monkeySee5()
    monkeySee6()
    monkeySee7()
    print("Round done!", i)

works = [work0, work1, work2, work3, work4, work5, work6, work7]
maxwork1 = max(works)
works.remove(maxwork1)
maxwork2 = max(works)
print(maxwork1 * maxwork2)

# Part dos