import math
import random

# Floor function
def floor(x):
    return math.floor(x)

# Returns n dice rolls
def dice(n):
    array = []
    for i in range(0, n):
        if len(array) < int(n):
            array.append(random.randint(1, 6))
    if len(array) == int(n):
        return array

# A cool iterative pattern (Actually, it is pretty boring!)
def randfib(k):
    array = []
    array.append(0)
    array.append(1)
    for i in range(2, k):
        f = random.randint(0, 1)
        array.append(array[i - 2] + a[f] * array[i - 1])
    return array

# Final Ratio
def ratio_randfib(k):
    array = []
    for i in range(1, k + 1):
        if randfib(i) == 0:
            array.append("-")
        else:
            array.append(str(randfib(i + 1)[i]/float(randfib(i)[i - 1])))
    return array

# HCF
def HCF(a, b):
    array = []
    for i in range(1, int(min(a, b))):
        if floor(max(a,b) / float(min(a,b))) == max(a, b) / float(min(a, b)):
         array.append(min(a, b))
        if floor((max(a, b) - i)/ float(min(a, b))) == (max(a, b) - i) / float(min(a, b)):
            array.append(HCF(min(a, b), i))
    return array[-1]

# Sum of all numbers in an array
def sum_array(a):
    sum = 0
    for i in range(0, len(a)):
        sum = sum + int(a[i])
    return sum

# Sum of all numbers in an array
def prod_array(a):
    prod = 1
    for i in range(0, len(a)):
        prod = prod * int(a[i])
    return prod

# String/Number to array
def fri(a):
    array = []
    for i in range(1, len(str(a)) + 1):
        array.append(str(a)[i - len(str(a)) - 1])
    return array

# Conversion of any base to decimal
def base_k_to_base_10(a, k):
    array = []
    for i in range(0, len(fri(a))):
        array.append(int(fri(a)[- i - 1]) * (k ** (i)))
    return sum_array(array)

# Knapsack Problem
# Shows optimal way to distribute money with least currencies
def ATM(a):
    array = []
    for i in range(0, a + 1):
        for j in range(0, int(a/2) + 2):
            for k in range(0, int(a/5) + 2):
                for l in range(0, int(a/25) + 2):
                    for m in range(0, int(a/50) + 2):
                        if i + 2 * j + 5 * k + 25 * l + 50 * m == a:
                            array.append([i, j, k, l, m])

    leastCount = sum_array(array[0])
    index = 0
    for n in range(0, len(array)):
        if leastCount > sum_array(array[n]):
            leastCount = sum_array(array[n])
            index = n

    return leastCount, array[index]

# Counts number of particular elements in a array
def count(a, b):
    Count = 0
    for i in range(0, len(a)):
        if a[i] == b:
            Count += 1
    return Count

def trunc(a, b, n):
    array = []
    count = 0
    for i in range(0, len(a)):
        array.append(a[i])
        if a[i] == b:
            count += 1
            if count ==  n:
                return array



def trunct(a, b, n):
    array = []
    count = 0
    for i in range(0, len(a)):
        array.append(a[i])
        if a[i] >= b:
            count += 1
            if count ==  n:
                return array, len(array)

# Dice cricket game, where 5 is out. n is number of balls
def cricket(n):
    array = dice(n)
    if count(array, 5) < 10:
        return sum_array(array) - (5 * count(array, 5))
    if count(array, 5) >= 10:
        return sum_array(trunc(array, 5, 10)) - 50

# Return array of a few scores from the cricket game
def array_cricket(a, b):
    array = []
    for i in range(0, a):
        array.append(cricket(b))
    return array

# Arithmetic Mean
def AM(a):
    return sum_array(a) / float(len(a))

# Geometric Mean
def GM(a):
    return prod_array(a) ** float((1/len(a)))

# Trying to find average score in particular overs
def array_am(a, b):
    array = []
    for i in range(0, a):
        array.append(AM(array_cricket(a, b)))
    return array

# A few functions for Rock, Paper, Scissors
def mainFunc(c, d, a, b):
    if a == "Rock" and b == "Paper":
        return d + " wins"
    if a == "Rock" and b == "Scissors":
        return c + " wins"
    if a == "Paper" and b == "Scissors":
        return d + " wins"
    if a == "Paper" and b == "Rock":
        return c + " wins"
    if a == "Scissors" and b == "Rock":
        return d + " wins"
    if a == "Scissors" and b == "Paper":
        return c + " wins"
    if a == b:
        print "It's a tie"
        return r_p_s()

f = ["Rock", "Paper", "Scissors"]
def r_p_s() :
    c = raw_input("Player1 name: ")
    d = raw_input("Player2 name: ")
    a = raw_input("Player1: ")
    b = random.choice(f)
    print mainFunc(c, d, a, b)

g = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
h = ["Rock", "Paper", "Scissors", "Lizard", "Spock", "Snake", "Element_119"]

# Rock, Paper, Scissors, Lizard, Spock
def mineFunc(c, d, a, b):
    if a == "Rock" and b == "Paper":
        return d + " wins"
    if a == "Rock" and b == "Scissors":
        return c + " wins"
    if a == "Rock" and b == "Lizard":
        return c + " wins"
    if a == "Rock" and b == "Spock":
        return d + " wins"
    if a == "Paper" and b == "Rock":
        return c + " wins"
    if a == "Paper" and b == "Scissors":
        return d + " wins"
    if a == "Paper" and b == "Lizard":
        return d + " wins"
    if a == "Paper" and b == "Spock":
        return c + " wins"
    if a == "Scissors" and b == "Rock":
        return d + " wins"
    if a == "Scissors" and b == "Paper":
        return c + " wins"
    if a == "Scissors" and b == "Lizard":
        return c + " wins"
    if a == "Scissors" and b == "Spock":
        return d + " wins"
    if a == "Lizard" and b == "Rock":
        return d + " wins"
    if a == "Lizard" and b == "Paper":
        return c + " wins"
    if a == "Lizard" and b == "Scissors":
        return d + " wins"
    if a == "Lizard" and b == "Spock":
        return c + " wins"
    if a == "Spock" and b == "Rock":
        return c + " wins"
    if a == "Spock" and b == "Paper":
        return d + " wins"
    if a == "Spock" and b == "Scissors":
        return c + " wins"
    if a == "Spock" and b == "Lizard":
        return d + " wins"
    if a == b:
        print "It's a tie. Try again !!!"
        return r_p_s_l_sp()

def r_p_s_l_sp():
    c = raw_input("Player1 name : ")
    d = raw_input("Player2 name : ")
    a = raw_input("Player1 : ")
    b = random.choice(g)
    print mineFunc(c, d, a, b)

# Rock, Paper, Scissors, Lizard, Spock, Snake, Element 119
def maneFunc(c, d, a, b):
    if a == "Rock" and b == "Paper":
        return d + " wins"
    if a == "Rock" and b == "Scissors":
        return c + " wins"
    if a == "Rock" and b == "Lizard":
        return c + " wins"
    if a == "Rock" and b == "Spock":
        return d + " wins"
    if a == "Rock" and b == "Snake":
        return c + " wins"
    if a == "Rock" and b == "Element_119":
        return d + " wins"
    if a == "Paper" and b == "Rock":
        return c + " wins"
    if a == "Paper" and b == "Scissors":
        return d + " wins"
    if a == "Paper" and b == "Lizard":
        return d + " wins"
    if a == "Paper" and b == "Spock":
        return c + " wins"
    if a == "Paper" and b == "Snake":
        return d + " wins"
    if a == "Paper" and b == "Element_119":
        return c + " wins"
    if a == "Scissors" and b == "Rock":
        return d + " wins"
    if a == "Scissors" and b == "Paper":
        return c + " wins"
    if a == "Scissors" and b == "Lizard":
        return c + " wins"
    if a == "Scissors" and b == "Spock":
        return d + " wins"
    if a == "Scissors" and b == "Element_119":
        return d + " wins"
    if a == "Scissors" and b == "Snake":
        return c + " wins"
    if a == "Lizard" and b == "Rock":
        return d + " wins"
    if a == "Lizard" and b == "Paper":
        return c + " wins"
    if a == "Lizard" and b == "Scissors":
        return d + " wins"
    if a == "Lizard" and b == "Spock":
        return c + " wins"
    if a == "Lizard" and b == "Snake":
        return d + " wins"
    if a == "Lizard" and b == "Element_119":
        return c + " wins"
    if a == "Spock" and b == "Rock":
        return c + " wins"
    if a == "Spock" and b == "Paper":
        return d + " wins"
    if a == "Spock" and b == "Scissors":
        return c + " wins"
    if a == "Spock" and b == "Lizard":
        return d + " wins"
    if a == "Spock" and b == "Snake":
        return d + " wins"
    if a == "Spock" and b == "Element_119":
        return c + " wins"
    if a == "Element_119" and b == "Rock":
        return c + " wins"
    if a == "Element_119" and b == "Paper":
        return d + " wins"
    if a == "Element_119" and b == "Scissors":
        return c + " wins"
    if a == "Element_119" and b == "Lizard":
        return d + " wins"
    if a == "Element_119" and b == "Spock":
        return d + " wins"
    if a == "Element_119" and b == "Snake":
        return c + " wins"
    if a == "Snake" and b == "Rock":
        return d + " wins"
    if a == "Snake" and b == "Paper":
        return c + " wins"
    if a == "Snake" and b == "Scissors":
        return d + " wins"
    if a == "Snake" and b == "Lizard":
        return c + " wins"
    if a == "Snake" and b == "Spock":
        return c + " wins"
    if a == "Snake" and b == "Element_119":
        return d + " wins"
    if a == b:
        print "It's a tie!!!"
        return r_p_s_l_sp_sn_el()

def r_p_s_l_sp_sn_el():
    c = raw_input("Player1 name : ")
    d = raw_input("Player2 name : ")
    a = raw_input("Player1 : ")
    b = random.choice(h)
    print maneFunc(c, d, a, b)
