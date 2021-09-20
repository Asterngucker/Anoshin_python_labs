import turtle as tr
tr.speed(1000)
tr.left(90)
def draw(r):
    for i in range(180):
        tr.left(2)
        tr.forward(r)
    for i in range(180):
        tr.right(2)
        tr.forward(r)
for i in range(10, 20, 2):
    draw(i / 10)
