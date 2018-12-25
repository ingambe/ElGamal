from Elgamal import *

def attackElGamal(public_key):
    '''
    Print the private key if she's founded
    Prove that it's important to choose a big random x to prevent attacks
    :param public_key: the public key tuple
    '''
    q = public_key[0]
    g = public_key[1]
    h = public_key[2]
    for i in range(1, q):
        if (g ** i) % q == h:
            print("FOUND !")
            print("Private key = {}".format(i))
            return

if __name__== "__main__":
    alice = Elgamal()
    bob = Elgamal()

    # El Gamal for string
    message = "Hello World !"
    alice_public_key = alice.publishPublicKey()
    bob_cipher = bob.cipher(alice_public_key, message)
    alice_decrypted = alice.unCipher(bob_cipher)
    print(alice_decrypted)

    # El Gamal for integers
    message = 42
    alice_public_key = alice.publishPublicKey()
    bob_cipher = bob.cipher(alice_public_key, message)
    alice_decrypted = alice.unCipher(bob_cipher)
    print(alice_decrypted)

    # El Gamal for float
    message = 124.58
    alice_public_key = alice.publishPublicKey()
    bob_cipher = bob.cipher(alice_public_key, message)
    alice_decrypted = alice.unCipher(bob_cipher)
    print(alice_decrypted)