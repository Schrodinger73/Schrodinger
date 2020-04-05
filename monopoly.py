import random


def sum_array(a):
    sum = 0
    for i in range(0, len(a)):
        sum = sum + int(a[i])
    return sum


def monty_hall(k):
    array = []
    for i in range(0, k):
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        if a == b:
            array.append(0)
        if a != b:
            array.append(1)
    return sum_array(array) / float(len(array))

a = [1, 2, 4, 7, 3]

def delete(a, b):
    array = []
    for i in range(0, len(a)):
        if i != b:
            array.append(a[i])
    return array

def max(a):
    max = a[0]
    for i in range(0, len(a)):
        if a[i] > max:
            max = a[i]
    return max

def min(a):
    minimum = a[0]
    for i in range(0, len(a)):
        if a[i] < minimum:
            minimum = a[i]
    return minimum

def index_min(a):
    for i in range(0, len(a)):
        if a[i] == min(a):
            return i

def ascend(a):
    f = [min(a)]
    array = a
    for i in range(0, len(a) - 2):
        array = delete(array, index_min(a))
        f.append(min(array))

    f.append(max(a))
    return f

def rsla(a):
    k = ascend(a).append(max(a))
    print k

print ascend(a)







