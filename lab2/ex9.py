import turtle as tr
import numpy as np
def st(r, n):
    a = r * 2 * np.sin(np.pi / n)
    return a
tr.penup()
tr.forward(10)
for n in range(3, 13, 1):
    tr.pendown()
    tr.left(90 * (1 + (2 / n)))
    for i in range(n):
        tr.forward(st(10 + 10 * (n - 3), n))
        tr.left(180 * ((2 / n)))
    tr.right(90 * (1 + (2 / n)))
    tr.penup()
    tr.forward(10)  
    
