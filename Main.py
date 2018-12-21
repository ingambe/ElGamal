from Elgamal import *

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
    message = "42"
    alice_public_key = alice.publishPublicKey()
    bob_cipher = bob.cipher(alice_public_key, message)
    alice_decrypted = alice.unCipher(bob_cipher)
    print(alice_decrypted)

    # El Gamal for float
    message = "124.58"
    alice_public_key = alice.publishPublicKey()
    bob_cipher = bob.cipher(alice_public_key, message)
    alice_decrypted = alice.unCipher(bob_cipher)
    print(alice_decrypted)