def partition(low, high):
    pivotitem = S[low]

    j = low
    for i in range(low+1, high+1):
        if S[i] < pivotitem:
            j += 1
            S[i], S[j] = S[j], S[i]

    S[low], S[j] = S[j], S[low]
    
    return j

def quicksort(low, high):
    if high > low:
        pivotpoint = partition(low, high)
        quicksort(low, pivotpoint-1)
        quicksort(pivotpoint+1, high)

S = [15, 22, 13, 27, 12, 10, 20, 25]
quicksort(0, len(S)-1)
print(S)
