import turtle as tr
tr.speed(1000)
tr.penup()
tr.goto(-300, 0)
tr.pendown()
def semicircle(r):
    for i in range(60):
        tr.right(3)
        tr.forward(r)
tr.left(90)
for i in range(5):
    semicircle(4)
    semicircle(1)
