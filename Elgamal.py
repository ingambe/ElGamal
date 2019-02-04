from Tools import *
from random import randint

class Elgamal:

    def __init__(self):
        '''
        The initialisation of ElGamal's protocol, initialise our public and private key
        '''
        self.q = generateBigSafePrimeNumber()
        self.g = generateGenerator(self.q)
        # we choose a big secret key to prevent from the attack
        self.sk = randint(min(2**4, int(self.q/2)), self.q)
        self.h = (self.g ** self.sk) % self.q
        # set of quadratic residual
        self.qr = []
        for i in range(0, self.q):
            if quadraticResidual(i, self.q):
                self.qr.append(i)

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
        quadratic_residual = []
        for i in range(0, q):
            if quadraticResidual(i, q):
                quadratic_residual.append(i)
        if type(m) == str:
            if m >= len(quadratic_residual):
                c2 = ""
            else:
                m = quadratic_residual[m]
                c2 = ""
                for character in m:
                    c2 = c2 + str(ord(character) * y) + ","
        else:
            if m >= len(quadratic_residual):
                c2 = -1
            else:
                m = quadratic_residual[m]
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
        if cipher == -1:
            print("ERREUR : Message plus grand que l'ordre du groupe cyclique")
            result = "ERROR"
        else:
            if type(cipher) == str:
                result = ""
                for character in cipher.split(','):
                    if character != '':
                     result = result + chr(int(int(character) / ((c1 ** self.sk) % self.q)))
            else:
                result = cipher / ((c1 ** self.sk) % self.q)
        result = self.qr.index(result)
        return result
