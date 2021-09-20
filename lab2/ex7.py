import turtle as tr
import numpy as np
k = 0.2
for f in range(1000):
    r = k * f
    x = r * np.cos(f / (2 * np.pi))
    y = r * np.sin(f / (2 * np.pi))
    tr.goto(x, y)
