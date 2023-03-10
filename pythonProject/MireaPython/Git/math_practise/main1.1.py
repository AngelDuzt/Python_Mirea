from math import *
def main(n, m):
    fsum = 0
    for i in range (1, n + 1):
        for j in range (1, m + 1):
            fsum += ceil(i) - 76 * j
    fsum *= 22
    f_sum = 0
    for i in range (1, n + 1):
        for j in range (1, m + 1):
            f_sum += 42 * j + 90 * j ** 4 - 8
    f_sum /= 31
    return fsum - f_sum
print(main(88, 80))