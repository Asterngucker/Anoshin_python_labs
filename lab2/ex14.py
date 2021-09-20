import turtle as tr
import numpy as np
n = int(input("n = "))
tr.left(180)
for i in range(n):
    tr.forward(200)
    tr.left(180 - (180 / n))
