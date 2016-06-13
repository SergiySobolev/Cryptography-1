#!/usr/bin/env python

# Cryptography 1 - Stanford University [Week 2 - Question 2]

import sys
from cryptohelper import *

k='140b41b22a29beb4061bda66b6747e14'.decode('hex')
ct='5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'.decode('hex')


def main(argv):
	print decrypt_block_CBC(ct[16:], 16, ct[:16], k, decrypt_block_AES)


if __name__ == "__main__":
	main(sys.argv)
