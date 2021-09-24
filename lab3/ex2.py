import turtle as tr
import numpy as np


n0 = ('pd', 'f', 'right', 'f', 'f', 'right', 'f', 'right', 'f', 'f', 'right', 'f', 'end')
n1 = ('pu', 'f', 'pd', 'half_left', 'left', 'left', 'f2', 'right', 'right', 'f2', 'right', 'half_right', 'f', 'f', 'right', 'right', 'f', 'f', 'right', 'end')
n2 = ('pd', 'f', 'right', 'f', 'half_right', 'f2', 'left', 'half_left', 'f', 'left', 'pu', 'f', 'f', 'right', 'end')
n3 = ('pd', 'f', 'right', 'half_right', 'f2', 'left', 'half_left', 'f', 'right', 'half_right', 'f2', 'pu', 'left', 'half_left', 'f', 'left', 'f', 'f', 'right', 'end')
n4 = ('pd', 'right', 'f', 'left', 'f', 'right', 'f', 'left', 'left', 'f', 'f', 'right', 'end')
n5 = ('pd', 'f', 'left', 'left', 'f', 'left', 'f', 'left', 'f', 'right', 'f', 'right', 'f', 'left', 'left', 'f', 'left', 'pu', 'f', 'f', 'right', 'end')
n6 = ('pd', 'f', 'left', 'left', 'f', 'left', 'f', 'f', 'left', 'f', 'left', 'f', 'left', 'f', 'left', 'left', 'f', 'left', 'pu', 'f', 'right', 'end')
n7 = ('pd', 'f', 'right', 'half_right', 'f2', 'half_left', 'f', 'pu', 'left', 'f', 'left', 'f', 'f', 'right', 'end')
n8 = ('pd', 'f', 'right', 'f', 'right', 'f', 'right', 'f', 'left', 'left', 'f', 'f', 'left', 'f', 'left', 'f', 'f', 'right', 'end')
n9 = ('pd', 'f', 'right', 'f', 'half_right', 'f2', 'left', 'left', 'f2', 'half_left', 'left', 'f', 'right', 'f', 'right', 'f', 'end')

l = 20

def bruh(a):    #переводит из команды в движение
    if (a == 'f'):
        tr.forward(l)
    elif (a == 'f2'):
        tr.forward(l * np.sqrt(2))
    elif (a == 'right'):
        tr.right(90)
    elif (a == 'half_right'):
        tr.right(45)
    elif (a == 'left'):
        tr.left(90)
    elif (a == 'half_left'):
        tr.left(45)
    elif (a == 'pu'):
        tr.penup()
    elif (a == 'pd'):
        tr.pendown()
    elif (a == 'end'):
        tr.penup()
        tr.forward(l)
    else:
        pass

list = input().split()
tr.penup()
tr.goto(-300, 0)

for i in range(len(list)):
    if (list[i] == '0'):
        for j in range(len(n0)):
            bruh(n0[j])
    elif (list[i] == '1'):
        for j in range(len(n1)):
            bruh(n1[j])
    elif (list[i] == '2'):
        for j in range(len(n2)):
            bruh(n2[j])
    elif (list[i] == '3'):
        for j in range(len(n3)):
            bruh(n3[j])
    elif (list[i] == '4'):
        for j in range(len(n4)):
            bruh(n4[j])
    elif (list[i] == '5'):
        for j in range(len(n5)):
            bruh(n5[j])
    elif (list[i] == '6'):
        for j in range(len(n6)):
            bruh(n6[j])
    elif (list[i] == '7'):
        for j in range(len(n7)):
            bruh(n7[j])
    elif (list[i] == '8'):
        for j in range(len(n8)):
            bruh(n8[j])
    elif (list[i] == '9'):
        for j in range(len(n9)):
            bruh(n9[j])
