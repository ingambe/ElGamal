from random import randint
from math import ceil, sqrt


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


def generateASmallerPrimeNumber(x, q):
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


def generateQuadtraticGenerator(p):
    '''
    Generate a quadratic residual generator of the cyclic group of order p (nammed Qp with p is safe prime) using the subgroup q
    When the order of group is prime, all element are generator
    x^2 mod order_of_groups is quadratic residual
    :param p: the order of the cyclic group
    :return: a generator
    '''
    q = int((p - 1) / 2)
    if not isSafePrime(p):
        raise Exception("p not safe prime")
    if not is_prime(q):
        raise Exception("q not prime, p not safe prime")
    generator = randint(2, min(2**4, q))
    if not isSafePrime(p):
        raise Exception("Safe prime needed")
    generator = (generator ** 2) % p
    if not quadraticResidual(generator, p):
        raise Exception("Generator need to be a quadratic residual")
    # test generator
    residual_generated = [lambda i: (0 if not quadraticResidual(i, p) else 1) for i in range(0, p)]
    for i in range(1, q):
        tmp = (generator ** i) % p
        if residual_generated[tmp] == 0:
            raise Exception("Not a quadratic generator")
        elif residual_generated[tmp] == 1:
            residual_generated[tmp] = 2
        elif residual_generated[tmp] == 2:
            raise Exception("Not a cyclic group")
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
    return is_prime(q) and is_prime((q - 1) / 2)
