def lmult(u, v):
    if 0 < len(u):
        i = u[0]
    else:
        i = 0

    if 0 < len(v):
        j = v[0]
    else:
        j = 0

    value = i*j
    carry = value//10

    result = []
    result.append(value%10)

    if carry > 0:
        result.append(carry)

    return result

def exp(u, m):
    if u == [0]:
        return [0]
    else:
        return ([0]*m)+u

def div(u, m):
    if len(u) < m:
        u.append(0)

    return u[m:len(u)]

def rem(u, m):
    if len(u) < m:
        u.apend(0)

    return u[0:m]

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

def prod(u, v):
    if len(u) > len(v):
        n = len(u)
    else:
        n = len(v)

    if len(u)==0 or len(v)==0:
        #print(u, v, [0])
        return [0]
    elif n <= threshold:
        return lmult(u, v)
    else:
        m = n // 2

        x = div(u, m)
        y = rem(u, m)
        w = div(v, m)
        z = rem(v, m)

        p1 = prod(x, w)
        p2 = ladd(prod(x, z), prod(w, y))
        p3 = prod(y, z)

        return ladd(ladd(exp(p1, 2*m), exp(p2, m)), p3)

threshold = 1

u = [2, 3, 8, 7, 6, 5]
v = [3, 2, 7, 3, 2, 4, 9]

print(567832 * 9423723)

print(prod(u, v)[::-1])
