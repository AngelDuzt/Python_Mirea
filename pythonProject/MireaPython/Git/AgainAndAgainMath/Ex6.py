from  Ex5 import alg
def algmatrix(A):
    un_A = []
    for i in range (0, len(A)):
        line = []
        for j in range(0, len(A)):
            line.append(alg(A, i, j))
        un_A.append(line)

    return un_A

A = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]

print(algmatrix(A))


