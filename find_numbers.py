# coding: UTF-8
import random
h = 0
b = 0
x = 0


a0 = random.randint(0,9)
a1 = random.randint(0,9)
a2 = random.randint(0,9)
a3 = random.randint(0,9)
a = [a0, a1, a2, a3]



for n in range(11):

    print "enter 4 numbers from 0 to 9"
    x0 = int(raw_input())
    x1 = int(raw_input())
    x2 = int(raw_input())
    x3 = int(raw_input())
    x = [x0, x1, x2, x3]

    for i in range(len(a)):
        if a[i] == x[i]:
            h += 1
        elif a[0] == x[i]:
            b += 1
        elif a[1] == x[i]:
            b += 1
        elif a[2] == x[i]:
            b += 1
        elif a[3] == x[i]:
            b += 1

    print "%d hit,%d blow" %(h,b)
