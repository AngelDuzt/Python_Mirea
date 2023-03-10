def main(y, z):
    n = len(y)
    s = 0
    for i in range (1, n + 1):
        s += abs(y[i-1] - z[i-1])
    return s

print(main([1, 0.5, 1], [0.5, 2, 1]))