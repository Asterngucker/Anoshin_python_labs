import turtle as tr
n = int(input("n = "))
for i in range(n):
    tr.forward(100)
    tr.stamp()
    tr.backward(100)
    tr.left(360/n)
