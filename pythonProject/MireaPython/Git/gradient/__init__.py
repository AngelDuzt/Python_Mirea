import math
from tkinter import *
import tkinter as tk
def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr
# Ваш код здесь:

def func(x, y):
    # pct_1 = ((0.55 - x) ** 2 + (0.55 - y) ** 2) ** 0.5
    # pct_2 = ((0.45 - x) ** 2 + (0.45 - y) ** 2) ** 0.5
    # return (0.5 - pct_1) * 3, (0.5 - pct_2) * 3, 0
    r = 1 - (2*x - 1.1) ** 2 - (2*y - 1.1) ** 2
    g = 1 - (2 * x - 0.9) ** 2 - (2 * y - 0.9) ** 2
    return r, g, 0
label = tk.Label()
tk.PhotoImage
img = tk.PhotoImage(data = pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image = img)
tk.mainloop()

