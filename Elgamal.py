from Tools import *
from random import randint

class Elgamal:

    def __init__(self, q = None, g = None, ah = None):
        '''
        The initialisation of ElGamal's protocol with the information
        g, q and ah are optional, empty if we are Alice
        :param q: the cycle group's order
        :param g: the generator
        :param ah: alice's h, None if we are Alice (the initialisator of the protocol)
        '''
        if q is None:
            self.q = generateBigPrimeNumber()
        else:
            self.q = q
        if g is None:
            self.g = generateASmallerPrimeNumber(self.q)
        else:
            self.g = g
        self.sk = randint(1, self.q)
        self.h = (self.g ** self.sk) % self.q
        self.ah = ah

    def publishPublicKey(self):
        '''
        :return: publish your public key
        '''
        return (self.q, self.g, self.h)



