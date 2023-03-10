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
    pct = ((0.5 - x) ** 2 + (0.5 - y) ** 2) ** 0.5
    pct_1 = ((0.6 - x) ** 2 + (0.33 - y) ** 2) ** 0.5
    if x > 0.5 and y < 0.5 and 0.6 - pct_1 > 0.35 and 0.33 - pct_1 > 0.3:
        return 0, 0, 0
    elif 0.5 - y > 2*(0.5 - x)/3 and x >= 0.5 and y >= 0.5:
        return 0, 0, 0
    elif 0.5 - y < -2*(0.5-x)/3 and x >= 0.5 and y <= 0.5:
        return 0, 0, 0
    elif 0.5 - pct > 0.2 and 0.5 - pct > 0.2:
        return 1, 1, 0
    else:
        return 0, 0, 0
label = tk.Label()
tk.PhotoImage
img = tk.PhotoImage(data = pyshader(func, 256, 256)).zoom(2, 2)
img_1 = tk.PhotoImage(data= pyshader(func, 256, 256)).zoom(2,2)
label.pack()
label.config(image = img)
tk.mainloop()

