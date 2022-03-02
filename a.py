def fibonacci(n):
    if not n:
        return 0
    
    a = 0
    b = 1

    for _ in range(1, n):
        temp = a + b
        a = b
        b = temp

    return b

def square(n):
    return n*n

def incr(n):
    return n+1