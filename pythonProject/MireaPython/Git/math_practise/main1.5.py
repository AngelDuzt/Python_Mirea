def main(y, z):
    n = len(y)
    array = []
    for i in range (1, n + 1):
        array.append(abs(y[i-1] - z[i-1]))
    return max(array)

print(main([1, 0.5, 1], [0.5, 2, 1]))