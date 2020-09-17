import math

def is_prime(a):
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    else:
            return True

def prime(a, b):
    array = []
    for i in range(a, b):
        if is_prime(i):
            array.append(i)
    return array

# Test for Collatz Conjecture.
def collatz(a):
    array = [a]
    while a != 1:
        if a % 2 == 0:
            array.append(a/2)
            a = a/2
        else:
            array.append(3 * a + 1)
            a = 3 * a + 1
    return array

# Test for Goldbach Conjecture.
def goldbach(a):
    for i in prime(2, a - 1):
        for j in prime(2, a - 1):
            if is_prime(i) and is_prime(j):
                if i + j == a:
                    return [i, j]