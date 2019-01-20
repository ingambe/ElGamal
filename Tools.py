from random import randint
from math import ceil, sqrt, gcd


def generateBigOddNumber():
    '''
    A big odd number generator
    :return: an odd number between 2**8 and 2**11
    '''
    return (2 * randint(2 ** 8, 2 ** 10)) + 1


def generateBigSafePrimeNumber():
    '''
    A big safe prime number generator
    :return: a big safe prime number (2**8 < x < 2**16)
    '''
    big_odd_number = generateBigOddNumber()
    while not (isSafePrime(big_odd_number)):
        big_odd_number -= 2
    return big_odd_number


def is_prime(x):
    '''
    Test the primality of a number
    :param x: the number to test
    :return: if x is prime or not
    '''
    if x % 2 == 0:
        return False
    # by steps of 2, avoid to check even number
    # stop at square of x to avoid useless check, because k * i = n with i > sqrt(n) is impossible
    # because it implies that k < sqrt(n) so it will have been already checked
    for i in range(3, ceil(sqrt(x)), 2):
        if x % i == 0:
            return False
    return True


def generateASmallerCoPrimeNumber(x, q):
    '''
    Generate a prime number smaller than x
    :param x: a prime number
    :return: a prime number smaller than x
    '''
    # generate a number between 2 and x-1
    startNumber = randint(2, x - 1)
    # if we haven't generate 2 and startNumber is even, we change startNumber to an odd number
    if startNumber != 2 and startNumber % 2 == 0:
        startNumber -= 1
    while not (is_prime(startNumber)) and startNumber > 2:
        startNumber -= 2
    return startNumber


def isAGenerator(g, q):
    '''
    Test if a number is a generator of a given cyclic group
    :param g: the generator
    :param q: the cyclic group order
    :return: if g is a generator of the cyclic groupe of q
    '''
    generated = [False for i in range(0, q)]
    i = 1
    while i < q:
        number = (g**i) % q
        if generated[number]:
            return False
        generated[number] = True
        i += 1
    return True

def minMaxGenerator(q):
    '''
    Generate the minimal and maximal generator of a cyclic group q
    :param q:
    :return:
    '''
    minimum = 2
    while not(isAGenerator(minimum, q)) and minimum < q:
        minimum += 1
    maximum = q - 1
    while not(isAGenerator(maximum, q)) and maximum > 1:
        maximum -= 1
    return minimum, maximum


def generateGenerator(q):
    '''
    Generate a generator of the cyclic group of order q
    :param q: the order of the cyclic group
    :return: a generator
    '''
    minimum, maximum = minMaxGenerator(q)
    generator = randint(minimum, maximum)
    upOrDown = randint(0, 1)
    if upOrDown == 0:
        while not(isAGenerator(generator, q)) or not coPrime(generator, q):
            generator -= 1
    else:
        while not(isAGenerator(generator, q)) or not coPrime(generator, q):
            generator += 1
    return generator


def quadraticResidual(a, q):
    '''
    Check if a number is a quadratic residual
    :param a: the number to test
    :param q: the order of the cyclic group
    :return: if a is a quadratic residual
    '''
    for i in range(1, q):
        if a % q == (i ** 2) % q:
            return True
    return False


def isSafePrime(q):
    return is_prime(q) and is_prime((2 * q) + 1)


def coPrime(p, q):
    return gcd(p, q) == 1
