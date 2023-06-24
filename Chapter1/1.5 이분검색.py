def binsearch(n, S, x):
    low = 0
    high = n-1

    while low<=high:
        mid = (low+high)//2
        if x == S[mid]:
            return mid
        elif x < S[mid]:
            high = mid - 1
        else:
            low = mid + 1

S = [4, 11, 6, 24, 21, 7, 8, 15, 33]
S.sort()
print(S)

print(binsearch(len(S), S, 8))
