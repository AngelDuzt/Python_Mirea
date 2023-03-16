def submatrix(args, i, j):
    return [row[:j] + row[j + 1:] for row in (args[:i] + args[i + 1:])]

A = [[0, 2, 1], [1, 4, 3], [2, 1, 1]]
print(submatrix(A, 0, 0))