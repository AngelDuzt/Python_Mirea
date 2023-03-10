def func1(y, z):
    n = len(y)
    s = 0
    for i in range (1, n + 1):
        s += (y[i-1] - z[i-1]) ** 2
    return s

print(func1([1, 0.5, 1], [0.5, 2, 1]))