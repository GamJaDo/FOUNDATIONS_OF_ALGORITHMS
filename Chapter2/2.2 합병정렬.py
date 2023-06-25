def merge(h, m, U, V, S):
    # mergesort부분의 S,U,V 는 주소가 다르다, 값은 같다.
    i, j, k = 0, 0, 0

    while i<h and j<m:
        if U[i] < V[j]:
            S[k] = U[i]
            i += 1
        else:
            S[k] = V[j]
            j += 1

        k += 1

    if i >= h:
        S[k:h+m] = V[j:m]
    else:
        S[k:h+m] = U[i:h]

def mergesort(n, S):
    # test부분의 S와는 주소가 다르다, 값은 같다.
    if n > 1:
        h = n//2
        m = n - h

        U = S[0:h]
        V = S[h:n]
        mergesort(h, U)
        mergesort(m, V)
        merge(h, m, U, V, S)

S = [27, 10, 12, 20, 25, 13, 15, 22]
mergesort(len(S), S)
print(S)
