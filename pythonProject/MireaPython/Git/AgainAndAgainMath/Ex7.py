from Ex3 import det
from Ex6 import algmatrix
def inv(A):
    det_A = det(A)
    matrix = algmatrix(A)
    matrix = Tranpose(matrix)
    for i in range (len(matrix)):
        for j in range (len(matrix)):
            matrix[i][j] = matrix[i][j] / det_A
    return matrix

def Tranpose(A):
    return [list(i) for i in zip(*A)]


A = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]

print(inv(A))
