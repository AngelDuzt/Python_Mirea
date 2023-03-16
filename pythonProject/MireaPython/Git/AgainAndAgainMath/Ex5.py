from Ex4 import minor
def alg(A, i, j):
    return pow(-1, i + j) * minor(A, i, j)

A = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]

print(alg(A, 1, 1))