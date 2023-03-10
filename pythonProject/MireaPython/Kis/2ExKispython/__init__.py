from math import *


def main(x):
    if x < 83:
        return sin(39 * x ** 3) + (x ** 5) / 48
    elif 83 <= x < 103:
        return 77 * (20 * x ** 2 - 83) ** 4
    elif 103 <= x < 139:
        return 0.11 + (1 - x / 49) ** 5 + 57 * log(x, 10) ** 3
    else:
        return 45 * (x ** 3 / 32) ** 3
