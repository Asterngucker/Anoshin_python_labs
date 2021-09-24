from random import randint
import turtle  as tr
import numpy as np

def goto_vector(dx, dy, turtle):  
    turtle.goto(turtle.xcor() + dx, turtle.ycor() + dy)
tr.speed(100)
tr.penup()
tr.goto(-300, -300)
tr.pendown()
for i in range(4):
    tr.forward(600)
    tr.left(90)
tr.ht()

Number_of_turtles = 10
step = 0.3
turtles = []
for i in range(Number_of_turtles):
    turtles.append(0)
for i in range(Number_of_turtles):
    turtles[i] = tr.Turtle()
    turtles[i].shape('circle')
    turtles[i].shapesize(1, 1)
    turtles[i].speed(0)
for i in range(Number_of_turtles):
    turtles[i].penup()
    turtles[i].goto(randint(-250, 250), randint(-250, 250))
speedx = []
speedy = []
v = [0] * Number_of_turtles
vx = [0] * Number_of_turtles
vy = [0] * Number_of_turtles
for i in range(Number_of_turtles):
    speedx.append(randint(-70, 70))
    speedy.append(randint(-70, 70))
while True:
    for i in range(Number_of_turtles):
        v[i] = np.sqrt(speedx[i]**2 + speedy[i]**2)
    for i in range(Number_of_turtles):
        if (abs(turtles[i].xcor() + (speedx[i] * step)) >= 300):  
            speedx[i] = -speedx[i]
        if (abs(turtles[i].ycor() + (speedy[i] * step)) >= 300):  
            speedy[i] = -speedy[i]
        for j in range(i + 1, Number_of_turtles, 1):
            if (np.sqrt((turtles[i].xcor() - turtles[j].xcor())**2 + (turtles[i].ycor() - turtles[j].ycor())**2) <= 20):
                p = [turtles[i].xcor() - turtles[j].xcor(), turtles[i].ycor() - turtles[j].ycor()]
                angle_p = 0
                if (p[0] != 0.0):
                    angle_p = np.arctan(p[1] / p[0])
                angle1 = np.arcsin(speedx[i] / np.sqrt(speedx[i]**2 + speedy[i]**2))
                angle2 = np.arcsin(speedx[j] / np.sqrt(speedx[j]**2 + speedy[j]**2))
                vx[i] = v[i] * np.sin((angle1 - angle_p))
                vy[i] = v[i] * np.cos((angle1 - angle_p))
                vx[j] = v[j] * np.sin((angle2 - angle_p))
                vy[j] = v[j] * np.cos((angle2 - angle_p))
                swap = vx[j]
                vx[j] = vx[i]
                vx[i] = swap
                angle1_new = np.arcsin(vy[i] / np.sqrt(vx[i]**2 + vy[i]**2)) - angle_p
                angle2_new = np.arcsin(vy[j] / np.sqrt(vx[j]**2 + vy[j]**2)) +-angle_p
                speedx[i] = np.cos(angle1_new) * np.sqrt(vx[i]**2 + vy[i]**2)
                speedy[i] = np.sin(angle2_new) * np.sqrt(vx[i]**2 + vy[i]**2)
                speedx[j] = -np.cos(angle1_new) * np.sqrt(vx[j]**2 + vy[j]**2)
                speedy[j] = -np.sin(angle2_new) * np.sqrt(vx[j]**2 + vy[j]**2)
        goto_vector(speedx[i] * step, speedy[i] * step, turtles[i])


