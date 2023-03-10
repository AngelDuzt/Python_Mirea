import math


def main(y, z):
    x1 = 39 * pow(((z / 20) - 80 * y * y), 7)
    x2 = 72 * pow(math.log(y), 6)
    x3 = 78 * pow((41 * (y ** 3) - 20 * (y ** 2) - z), 7)
    x5 = 23 * pow(math.cos(1 - y ** 3 - z), 4)
    f = (x1 / (x2 + x3)) + x5
    return f

