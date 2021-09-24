import turtle as tr
import numpy as np
tr.speed(100)
x = -300
y = 0
vx = 50
vy = 100
dt = 0.01
ay = -50
tr.speed(1000)
tr.goto(1000, 0)
tr.goto(-1000, 0)
tr.goto(-300, 0)
tr.speed(1)
while 1:
    print(y)
    if ((y > -1.0) and (y < 1.0)) and (vy < 0):
        vy = -vy * 0.8
        vx = vx * 0.8
    x += vx*dt
    y += vy*dt + ay*dt**2/2
    vy += ay*dt
    tr.goto(x, y)
