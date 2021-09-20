import turtle as tr
for n in range(1, 11, 1):
    for i in range(4):
        tr.forward(10 * n)
        tr.left(90)
    tr.penup()
    tr.right(135)
    tr.forward(7)
    tr.left(135)
    tr.pendown()
