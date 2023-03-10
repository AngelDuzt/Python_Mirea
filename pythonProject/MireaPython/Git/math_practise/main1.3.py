def main(y, z):
    n = len(y)
    s = 0
    for i in range (1, n + 1):
        s += (y[i-1] - z[i-1]) ** 2
    return s ** 0.5

print(main([1, 0.5, 1], [0.5, 2, 1]))