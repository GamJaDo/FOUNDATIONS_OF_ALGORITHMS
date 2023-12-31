def floyd(W):
    D = W
    n = len(W)
    for k in range(n):
        print(k)
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k]+D[k][j])

    return D

INF = 999
W = [[0, 1, INF, 1, 6],
     [9, 0, 3, 2, INF],
     [INF, INF, 0, 4, INF],
     [INF, INF, 2, 0, 3],
     [3, INF, INF, INF, 0]
     ]

D = floyd(W)
for i in range(len(D)):
    print(D[i])
