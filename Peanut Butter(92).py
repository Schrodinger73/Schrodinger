import math

# To check if a number is prime
def is_prime(a):
    if a==1:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
   
    return True


# A perfect number is a number which's all proper factors is equal to the number itself.
def perfect(a, b):
    array = []
    for i in range(a, b):
        if is_prime((2 ** i) - 1):
            array.append(((2 ** (i - 1)) * ((2 ** i) - 1), (2 ** i) - 1, i))
    return array

# Returns all primes in a range
def prime(a, b):
    array = []
    for i in range(a, b + 1):
        if is_prime(i):
            array.append(i)
    return array

# Returns twin primes in a range
def twin_primes(a, b):
    array = []
    for i in range(int(a + 2), b):
        if is_prime(i) and is_prime(i - 2):
            array.append((int(i)))
    return array

# Returns average of all primes in a Range.
def avg_prime(a, b):
    num_array = [i for i in range(a,b) if is_prime(i)]
    return sum(num_array) / len(num_array)

# Returns average of the endpoint primes in a Range.
# This and and the previous function are interlinked, and both averages are pretty close.
def new_avg_primes(a, b):
    return float((b - a + 1))/len(prime(a, b))

# Converts an Array to a Number.
def a2n(a):
    f = 0
    for i in range(0, len(a)):
        f = f + int(a[i]) * (10 ** (len(a) - 1 - i))
    return f

# Reverses a number.
def reverse_num(a): #Reverse is already a python thing
    num = str(a)[::-1]
    return int(num)

# Returns reversible primes in a range.
def rev_prime(a, b):
    array = []
    for i in range(a, b):
        if is_prime(i) and is_prime(reverse_num(i)) and i > reverse_num(i):
            array.extend([i, reverse_num(i), "|"])
    return array

# Product of all numbers in an array.
def prod(a):
    return math.prod(a)

# Returns Factorial of a number.
def factorial(a):
    product = 1
    for i in range(1, a + 1):
        product = product * i
    return product

# My formula for finding large primes, based on Euclid's proof of infinite primes.
def huge_primes(n):
    return prod(prime(1, n)) + 1
