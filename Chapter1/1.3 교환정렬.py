def exchange(S, n):
    
    for i in range(n-1):
        for j in range(i+1, n):
            if S[j] < S[i]:
                S[j], S[i] = S[i], S[j]
            

S = [5, 1, 7, 3, 4]

exchange(S, len(S))
print(S)
