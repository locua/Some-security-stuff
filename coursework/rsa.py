import binascii, sys
from helpers import *
import argparse

class RSA:
    """
        RSA class with encryption and decryption methods
    """
    def __init__(self):
        pass

    def encrypt(self, message, pub):
        print("message: ", message)
        m = self.string_to_int(message)
        block_size = None
        assert m < pub["n"]
        print("m: ", m)
        cipher = pow(m, pub["e"], pub["n"])
        print("c: " , cipher, "\n")
        return cipher

    def decrypt(self, c, d, pub):
        # m = c^d mod n
        assert c < pub["n"]
        plaintext = pow(c, d, pub["n"])
        return self.int_to_string(plaintext)

    def string_to_int(self, s):
        # https://stackoverflow.com/questions/12625627/python3-convert-unicode-string-to-int-representation

        # encode as utf-8, convert bytes to hexcodes as bytestring...
        # and convert to int specifying base 16(hex)
        i  = int(binascii.hexlify(s.encode('utf-8')), 16)
        #print(i)
        return i

    def int_to_string(self, i):
        # convert int to hex, unhexlify and decode
        return binascii.unhexlify(hex(i)[2:]).decode('utf-8')

    def generateKeys(self, keysize=870):
        # generate two large primes p and q (each approx 100 digits)
        p = generate_prime_number(keysize)
        #print(len(str(p)))
        q = generate_prime_number(keysize)
        #print(len(str(q)))
        # computer n = p*q
        n = p*q
        r = (p - 1) * (q - 1)
        print("SIZE OF r in bits", sys.getsizeof(r)*8)
        # choose large prime e: 1 < e < r
        e = randbelow(r)
        e = 11
        #Use Euclid's Algorithm to verify that e and phi(n) are comprime
        g = math.gcd(e, r)
        while g != 1:
            e = randbelow(r)
            g = math.gcd(e, r)

        d = modinv(e, r)
#         print("Size of d in bits", sys.getsizeof(d)*8)
        # keeps d private publish pair(e, n) {public key
        public = {"e" : e, "n": n}
        private = d
        return (public, private)

def main():
    # rsa class
    rsa = RSA()
    # generate keys
    public, private = rsa.generateKeys()
    print("Public keys\n", "e: ", public["e"],",","n: ", public["n"])
    print("\nPrivate key\nd: ", private, "\n\n")

    c = rsa.encrypt("Hey hows it going you big old fart hows it going you big old fart", public)
    m = rsa.decrypt(c, private, public)
    print(m)

# execute main
if __name__ == "__main__":
    main()
