def seqsearch(S, x, n):
    location = 0
    while location<=n-1 and S[location]!=x:
        location += 1
        
        if location > n:
            location = 0
            break

    return location

S = [10, 7, 11, 5, 13, 8]
print(seqsearch(S, 5, len(S)))
