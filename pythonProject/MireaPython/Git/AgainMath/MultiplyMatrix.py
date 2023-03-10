def MultiplyMatrix(arr_1, arr_2):
    counter = 0
    summ = 0
    arr_len = len(arr_1)
    wire_len = len(arr_2[0])
    arr = [[0 for row in range(arr_len)] for col in range(wire_len)]
    for i in range(0, len(arr_1)):
        for j in range(0, len(arr_2[0])):
            for k in range(0, len(arr_2[0])-1):
                arr[i][j] += arr_1[i][k] * arr_2[k][j]
    return arr

print(MultiplyMatrix([[1, 2], [3, 4], [5, 6]], [[1, 2, 3], [4, 5, 6]]))
