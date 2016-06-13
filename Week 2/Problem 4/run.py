#!/usr/bin/env python

# Cryptography 1 - Stanford University [Week 2 - Question 4]

import sys
from cryptohelper import *

k='36f18357be4dbd77f050515c73fcf9f2'.decode('hex')
ct='770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'.decode('hex')


def main(argv):
	print decrypt_block_CTR(ct[16:], 16, ct[:16], k, encrypt_block_AES, False)
       

if __name__ == "__main__":
        main(sys.argv)
