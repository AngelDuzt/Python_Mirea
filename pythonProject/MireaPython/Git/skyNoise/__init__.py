import calendar
import time
from math import floor, sin
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

def clamp(minimum, x, maximum):
    return max(minimum, min(x, maximum))
# Ваш код здесь:
def func(x, y):
    sx = 10 * x
    sy = 10 * y
    color = fbm(sx, sy)
    return 0.3, color, 0.9
def random(x, y):
    return fract(sin(x * 12.1898 + y * 78.733) * 53758.5453123)

def fract(z):
    return z - floor(z)

def val_noise(x, y):
    ix = floor(x)
    fx = fract(x)

    iy = floor(y)
    fy = fract(y)

    ux = fx * fx * (3.0 - 2.0 * fx)
    uy = fy * fy * (3.0 - 2.0 * fy)

    return lerp(uy, lerp(ux, random(ix + 0.0, iy + 0.0), random(ix + 1.0, iy + 0.0)),
                lerp(ux, random(ix + 0.0, iy + 1.0), random(ix + 1.0, iy + 1.0)))

def lerp(x, a, b):
    return (1 - x) * a + x * b

def fbm(x, y):
    value = 0.
    amplitude = .5
    frequency = 0.
    for i in range (0, 6):
        value += amplitude * val_noise(x, y)
        x *= 2.
        y *= 2.
        amplitude *= .5
    return value


label = tk.Label()
tk.PhotoImage
img = tk.PhotoImage(data = pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image = img)
tk.mainloop()

