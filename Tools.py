from random import randint
from math import ceil, sqrt


def generateBigOddNumber():
    '''
    A big odd number generator
    :return: an odd number between 2**8 and 2**16
    '''
    return (2 * randint(2 ** 8, 2 ** 16)) + 1


def generateBigPrimeNumber():
    '''
    A big prime number generator
    :return: a big prime number (2**8 < x < 2**16)
    '''
    big_odd_number = generateBigOddNumber()
    while not (is_prime(big_odd_number)):
        big_odd_number = generateBigOddNumber()
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


def generateASmallerPrimeNumber(x):
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
