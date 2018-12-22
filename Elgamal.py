from Tools import *
from random import randint

class Elgamal:

    def __init__(self):
        '''
        The initialisation of ElGamal's protocol, initialise our public and private key
        '''
        self.q = generateBigPrimeNumber()
        self.g = generateASmallerPrimeNumber(self.q)
        # we choose a big secret key to prevent from the attack
        self.sk = randint(2**4, self.q)
        self.h = (self.g ** self.sk) % self.q

    def publishPublicKey(self):
        '''
        :return: publish your public key
        '''
        return self.q, self.g, self.h

    def cipher(self, pk, m):
        '''
        Cipher a message from a public key
        :param pk: Alice's public key (tuple q,g,h)
        :param m: the message to cipher
        :return: a tuple containing an information about the random x picked and the cipher
        '''
        q = pk[0]
        g = pk[1]
        h = pk[2]
        r = randint(1, q)
        c1 = (g ** r) % q
        y = (h ** r) % q
        if type(m) == str:
            c2 = ""
            for character in m:
                c2 = c2 + str(ord(character) * y) + ","
        else :
            c2 = m * y
        return c1, c2

    def unCipher(self, cipher):
        '''
        Decrypt the cipher
        :param cipher: a tuple containing C1 (g**r mod q) from Bob and the cipher, which could be a str or a number
        :return: the unencrypted message
        '''
        c1 = cipher[0]
        cipher = cipher[1]
        if type(cipher) == str:
            result = ""
            for character in cipher.split(','):
                if character != '':
                 result = result + chr(int(int(character) / ((c1 ** self.sk) % self.q)))
        else:
            result = cipher / ((c1 ** self.sk) % self.q)
        return result