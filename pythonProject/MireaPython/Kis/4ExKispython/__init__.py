from math import *


def main(n):
    if n == 0:
        return 0.58
    else:
        return main(n - 1) + 1 + log(97 + main(n - 1) ** 3, 2) ** 2 / 6
