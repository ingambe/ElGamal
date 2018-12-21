from Elgamal import *

if __name__== "__main__":
    alice = Elgamal()
    bob = Elgamal()
    print(alice.unCipher(bob.cipher(alice.publishPublicKey(), 123)))