def main(n, m):
    fsum = 0
    for k in range(1, m + 1):
        for i in range(1, n + 1):
            fsum += 79 * (74 * i ** 3 - k ** 2) ** 4 + (k ** 2 / 30) ** 7

    return fsum
