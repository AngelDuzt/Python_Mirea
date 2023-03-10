def refunc(y, z):
    h = 5
    n = len(y)
    s = 0
    for i in range (1, n + 1):
        s += abs(y[i-1] - z[i-1]) ** h
    return s ** (1/h)

print(refunc([1, 0.5, 1], [0.5, 2, 1]))