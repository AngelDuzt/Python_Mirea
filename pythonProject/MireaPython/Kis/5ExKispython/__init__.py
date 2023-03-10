from math import *


def main(array_z, array_x, array_y):
    fsum = 0
    n = len(array_z)
    for i in range(1, n + 1):
        z = array_z[i - 1] ** 3
        x = 38 * array_x[n - i]
        y = array_y[n - ceil(i / 4)] ** 2
        fsum += 98 * (z + x + y) ** 7
    return fsum * 71
