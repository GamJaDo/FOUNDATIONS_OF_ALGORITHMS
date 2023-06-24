def matrixmult(n, A, B, C):
    for i in range(n):
        for j in range(n):
            C[i][j] = 0

            for k in range(n):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]

A = [[2, 3], [4, 1]]
B = [[5, 7], [6, 8]]
C = [[0, 0], [0 ,0]]

matrixmult(len(A), A, B, C)

for i in C:
    for j in i:
        print(j, end = ' ')

    print()
