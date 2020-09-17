# Returns Pythogoras Triplets in a Range.
def pytho(a, b):
    array = []
    for i in range(1, a + 1):
        for j in range(1, a + 1):
            for k in range(2, b + 1):
                for l in range(1, k):
                    if i ** 2 + j ** 2 == a ** 2:
                        array.extend([min(i, j), max(j, i), a, "|"])
                    if l ** 2 + a ** 2 == k ** 2:
                        array.extend([min(l, a), max(a, l), k, "|"])
            return array



# Checks if a string is a Palindrome.
def palindrome(a):
    for i in range(0, len(str(a)) - 1):
            if str(a)[i] != str(a)[len(str(a)) - i - 1]:
                return False
    else:
       return True

# Lists out Palindromes in a given Range.
def pal_list(a, b):
    array = []
    for i in range(a, b + 1):
        if palindrome(i):
            array.append(i)
    return array


# Returns a number as a sum of three Palindromes. [Array of all possible triplets]
def three_pal(a):
    array = []
    for i in pal_list(11, a - 19):
        for j in pal_list(11, a - 2):
            for k in pal_list(11, a - 2):
                    if i <= j and j <= k:
                        if i + j + k == a:
                            array.append([i, j, k])
    return array




