import math
import random

def ln(x):
    return math.log(x, math.e)

def exp(s):
    if s == "engineer":
        return 3
    if s == "Engineer":
        return 3
    else:
        return math.e ** s

def pi(r):
    if r == "engineer":
        return 3
    if r == "Engineer":
        return 3
    else:
        return math.pi

def tau(z):
    return 2 * math.pi

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def arccos(x):
    return math.acos(x)

def arcsin(x):
    return math.asin(x)

def arctan(x):
    return math.atan(x)

def floor(x):
    return math.floor(x)

def ceiling(x):
    return math.ceil(x)

def fractional(x):
    return x - floor(x)


def H(w):
    sum = 0
    for i in range(1, w + 1):
        sum = sum + 1/float(i)
    return sum

def euler(w):
    return H(4000000) - ln(4000000)


def prod(a):
    product = 1
    for i in range(0, len(a)):
        product = product * a[i]
    return product


def factorial(a):
    product = 1
    for i in range(1, a + 1):
        product = product * i
    return product


def newH(z):
    Sum = 0
    for i in range(1, 400001):
        Sum = Sum + 1/float(z + i)
    return Sum


def in_prod(z):
    array = []
    for i in range(1, 3000000):
        array.append(i * ((exp(1)) ** (z/float(i)))/(float(i) + z))
    return array


def cal(z):
    return prod(in_prod(float(z)))


def factorial_real(z):
    if int(z) != z:
        return cal(z) / (float(math.e) ** (euler(1) * z))
    else:
        return factorial(z)

def Gamma(a):
    return factorial_real(a - 1)


def Beta(a, b):
    return Gamma(a) * Gamma(b) / float(Gamma(a + b))


def W(a):
    i = random.randint(0, 200)
    while int(100000 * ((i * (exp(i)) - a) / (i * (exp(i)) + (exp(i))))) != 0:
        i = i - ((i * (exp(i)) - a)/(i * (exp(i)) + (exp(i))))
    if int(100000 * ((i * (exp(i)) - a)/(i * (exp(i)) + (exp(i))))) == 0:
        return i


def inv_xtothex(a):
    return exp(W(ln(a)))

def ReimannZeta(s):
    Sum = 0
    for i in range(1, 203998):
        if s > 1:
            Sum = Sum + 1 / float(i ** s)
        else:
            return "DNC"

    return Sum



def DiGamma(z):
    return H(399999) - euler(z) - newH(z - 1)

def GammaPrime(z):
    return float(DiGamma(z)) * Gamma(z)

def V(z):
    return Gamma(2 + W(inv_xtothex(ReimannZeta(Gamma(2 + W(inv_xtothex(ReimannZeta(1 + euler(z)))))))))

def cis(x):
    return str(cos(x)) + " + " + str(sin(x)) + "i"



def Volumenthdimension(n):
    return str((pi(2) ** (n/2))/Gamma(n)) + " r^" + str(n)

def superfactorial_1(n):
    array = []
    for i in range(1, n + 1):
        array.append(factorial(i))
    return array

def superfactorial(n):
    return prod(superfactorial_1(n))

def x_to_the_i(a):
    return cis(ln(a))

def aCb(a, b):
    if a < b:
        return 0
    else:
        return factorial_real(a) / (factorial_real(b) * factorial_real(a - b))

def aPb(a, b):
    if a < b:
        return 0
    else:
        return factorial_real(a) / factorial_real(a - b)

def i_to_the_x(a):
    return cis(pi(a) * a /2)


a = [[0, 0, 0], [0, 2, 3], [0, 1, 7]]

def tictactoe(k):
    for i in range(0, 3):
        if k[i][1] == k[i][0] and k[i][1] == k[i][2]:
            print "Row"
        if k[0][i] == k[2][i] and k[1][i] == k[2][i]:
            print "Column"
        if k[1][1] == k[2][2] and k[2][2] == k[0][0]:
            print "Diagonal"
        if k[0][2] == k[1][1] and k[1][1] == k[2][0]:
            print "Diagonal"
        else:
            print False

def ticrow(k):
    for i in range(0, 3):
        if k[i][1] == k[i][0] and k[i][1] == k[i][2]:
            return True

    return False

def ticcol(k):
    for i in range(0, 3):
        if k[0][i] == k[2][i] and k[1][i] == k[2][i]:
            return True

    return False


def ticdiag(k):
    for i in range(0, 3):
        if k[1][1] == k[2][2] and k[2][2] == k[0][0]:
            return True
        if k[0][2] == k[1][1] and k[1][1] == k[2][0]:
            return True

    return False

def ticpapa(k):
    if ticrow(k):
        print "Row"
    elif ticcol(k):
        print "Col"
    elif ticdiag(k):
        print "Diag"


a = ["M", "K"]


def odds(n):
    array = []
    for i in range(0, n):
        k = random.randint(0, 1)
        array.append(k)
    return array, sum(array) / float(n)


def tantan(a, b):
    array = []
    for i in range(a, b + 1):
        if (tan(i))**2 > (i)**2:
            array.append(i)
    print array

tantan(1, 2000000)

