from Ex3 import det
from Ex3 import submatrix
def minor(A, i, j):
    return det(submatrix(A, i, j))

A = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]

print(minor(A, 0, 1))
