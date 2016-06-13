#!/usr/bin/env python

# Cryptography 1 - Stanford University [Week 2 - Question 3]

import sys
from cryptohelper import *

k='36f18357be4dbd77f050515c73fcf9f2'.decode('hex')
ct='69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'.decode('hex')


def main(argv):
	print decrypt_block_CTR(ct[16:], 16, ct[:16], k, encrypt_block_AES, False)
       

if __name__ == "__main__":
        main(sys.argv)
