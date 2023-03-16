from Ex1 import smalldet
from Ex2 import submatrix
from Ex3 import det
from Ex4 import minor
from Ex5 import alg
from Ex6 import algmatrix
from Ex7 import Tranpose



def inv(a):
    cofactors = Tranpose(algmatrix(a))
    determinant = det(a)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant
    return cofactors


def multiply(x, y):
    return [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*y)] for X_row in x]


def moore_penrose(h):
    h_transposed = Tranpose(h)
    return multiply(
        inv(multiply(h_transposed, h)),
        h_transposed
    )


A = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]

print(moore_penrose(A))