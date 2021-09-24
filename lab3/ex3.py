import turtle as tr
import numpy as np

l = 20    #размер шрифта

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

list = input().split()    #считываем список чисел (через пробел!!! например 1 2 3 4 5)
tr.penup()
tr.goto(-300, 0)
fond = open('fond.txt', 'r')
for x in range(10):
    exec(fond.readline())    #считываем шрифт 
    
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
fond.close()
