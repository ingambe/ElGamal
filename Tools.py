from random import randint

# return an odd number between 2**16 and 2**31
def generateBigOddNumber():
    return (2 * randint(2 ** 16, 2 ** 31)) + 1


# return a big prime number (2**16 < x < 2**32)
def generateBigPrimeNumber():
    big_odd_number = generateBigOddNumber()
    while not (is_prime(big_odd_number)):
        big_odd_number = generateBigOddNumber()
    return big_odd_number


# test the primality of a number
def is_prime(x):
    if x % 2 == 0:
        return False
    # par pas de 2, evite de checker les nombres pair, on s'arretes a racine carree de x
    # + 2 à cause de l'aroundie possiblement à l'inférieur
    for i in range(3, round(sqrt(x)) + 2, 2):
        if x % i == 0:
            return False
    return True


def generateASmallerPrimeNumber(x):
    # generate a number between 2 and x-1
    startNumber = randint(2, x)
    # if we haven't generate 2 and startNumber is even, we change startNumber to an odd number
    if startNumber != 2 and startNumber % 2 == 0:
        startNumber -= 1
    while not (is_prime(startNumber)) and startNumber > 2:
        startNumber -= 2
    return startNumber
