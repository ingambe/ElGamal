from random import randint
from math import sqrt

def generateBigOddNumber():
    return (2 * randint(2**16, 2**31)) + 1

def generateBigPrimeNumber():
    big_odd_number = generateBigOddNumber()
    while not(is_prime(big_odd_number)):
        big_odd_number = generateBigOddNumber()
    return big_odd_number

def is_prime(x):
    if x % 2 == 0:
        return False
    # par pas de 2, evite de checker les nombres pair, on s'arretes a racine carree de x
    # + 2 à cause de l'aroundie possiblement à l'inférieur
    for i in range(3, round(sqrt(x)) + 2, 2):
        if x % i == 0:
            return False
    return True

print(generateBigPrimeNumber())