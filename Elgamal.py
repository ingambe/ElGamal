from Tools import *
from random import randint

class Elgamal:

    def __init__(self):
        '''
        The initialisation of ElGamal's protocol, initialise our public and private key
        '''
        self.q = generateBigPrimeNumber()
        self.g = generateASmallerPrimeNumber(self.q)
        self.sk = randint(1, self.q)
        self.h = (self.g ** self.sk) % self.q

    def publishPublicKey(self):
        '''
        :return: publish your public key
        '''
        return (self.q, self.g, self.h)

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
        '''
        cipher = ""
        for character in m:
            cipher = cipher + str(ord(character) * c2) + ","
        '''
        c2 = m * y
        return (c1, c2)

    def unCipher(self, cipher):
        c1 = cipher[0]
        cipher_text = cipher[1]
        '''
        result = ""
        for character in cipher_text.split(','):
            if character != '':
                result = result + chr(int(int(character) / (c1 ** self.sk)))
        '''
        result = cipher_text / ((c1 ** self.sk) % self.q)
        return result