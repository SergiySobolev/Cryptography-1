#!/usr/bin/env python

# Cryptography 1 - Stanford University [Week 3 - Question 1]

import sys
import hashlib
from cryptohelper import *


def calc_digest(data):
	chunks = block_split(data, 1024)

	for i in range(len(chunks)-1, 0, -1):
        	chunks[i-1] = chunks[i-1] + hashlib.sha256(chunks[i]).digest()

	return hashlib.sha256(chunks[0])

def main(argv):
	if len(argv) < 2:
		print "Using style:\n\trun.py <filename>\n"
		sys.exit(0)

	with open(argv[1]) as f:
 		data = f.read()

	d = calc_digest(data)
	print d.hexdigest()

if __name__ == "__main__":
        main(sys.argv)
