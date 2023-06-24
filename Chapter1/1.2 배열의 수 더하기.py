def numberSum(S, n):
    result = 0

    for i in range(n):
        result += S[i]

    return result

S = [1, 2, 3, 4, 5]
print(numberSum(S, len(S)))
