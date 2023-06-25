def location(S, low, high, x):
    if low > high:
        return False
    else:
        mid = (low+high)//2
        if x == S[mid]:
            return mid
        elif x < S[mid]:
            return location(S, low, mid-1, x)
        else:
            return location(S, mid+1, high, x)

S = [10, 12, 13, 14, 18, 20, 25, 27, 30, 35, 40, 45, 47]

print(location(S, 0, len(S)-1, 20))
