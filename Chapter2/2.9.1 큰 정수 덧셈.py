def ladd(u, v):

    result = []
    carry = 0
    
    if len(u) > len(v):
        n = len(u)
    else:
        n = len(v)

    for k in range(n):
        if k < len(u):
            i = u[k]
        else:
            i = 0

        if k < len(v):
            j = v[k]
        else:
            j = 0

        value = i + j + carry
        carry = value//10

        result.append(value%10)

    if carry > 0:
        result.append(carry)

    return result

u = [3, 2, 1]
v = [5, 4]

print(123 + 45)
print(ladd(u, v)[::-1])

u = [2, 3, 8, 7, 6, 5]
v = [3, 2, 7, 3, 2, 4, 9]

print(567832 + 9423723)
print(ladd(u, v)[::-1])
