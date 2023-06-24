def fib(n):
    temp = [0]*n

    temp[0] = 1
    temp[1] = 1
    
    if n > 0:
        for i in range(2, n):
            temp[i] = temp[i-1] + temp[i-2]

    return temp[n-1]

print(fib(100))
