from Tools import *
from random import randint

class Elgamal:

    # ah = alice's h, None if we are Alice (the initialisator of the protocol)
    def __init__(self, q = None, g = None, ah = None):
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

    # publish the public key
    def publishPublicKey(self):
        return (self.q, self.g, self.h)



