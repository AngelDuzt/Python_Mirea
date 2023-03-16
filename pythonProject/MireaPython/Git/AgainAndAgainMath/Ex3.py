from Ex1 import smalldet

def submatrix(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def det(a, i=0):
    if len(a) == 2:
        return smalldet(a)
    determinant = 0
    for j in range(len(a)):
        determinant += (-1) ** (i + j) * a[i][j] * det(submatrix(a, i, j))
    return determinant


A = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]
print(det(A, 0))
