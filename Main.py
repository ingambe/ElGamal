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

    # El Gamal for integer

    # TODO VERIFY GENERATOR

    print("Integer")
    message = 5
    alice_public_key = alice.publishPublicKey()
    print("Vous essayer de crypter {}".format(message))
    print("la clef publique de alice : {}".format(alice_public_key))
    print("l'ordre dy groupe cyclique est : {}".format(alice_public_key[0]))
    print(alice_public_key)
    bob_cipher = bob.cipher(alice_public_key, message)
    print("le crypte : {}".format(bob_cipher))
    alice_decrypted = alice.unCipher(bob_cipher)
    print("le message decrypte {}".format(alice_decrypted))
