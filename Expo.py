import math


def is_prime(a):
    if a == 0:
        return False
    if a == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(a)) + 1):
            if a % i == 0:
                return False
        else:
                return True


def sub(a, b):
    return int(a) - int(b)

def fi(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    secondLastFib = 0
    lastFib = 1
    current = secondLastFib + lastFib
    for i in range(2,n):
        current = secondLastFib + lastFib
        secondLastFib = lastFib
        lastFib = current

    return current


def prime_fib(a, b):
    array = []
    for i in range(a, b + 1):
        if is_prime(int(fi(i))):
            array.append([int(fi(i)), i])
    return array

print fi(1000000)

