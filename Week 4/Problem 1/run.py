#!/usr/bin/env python

# Cryptography 1 - Stanford University [Week 4 - Question 1]

import sys
import urllib2
from cryptohelper import *
import sys


ct = 'f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'.decode('hex')
charset=''.join([chr(i) for i in range(0,256)])

TARGET = 'http://crypto-class.appspot.com/po?er='


# Chaing one byte t string [Manually]
def str_set_chr(s, idx, value):
	s = list(s)
	s[idx] = value
	return ''.join(s)

def padding_oracle_request(ct):
	url = TARGET + ct.encode('hex')
	req = urllib2.Request(url)
	try:
		f = urllib2.urlopen(url)
	except urllib2.HTTPError, e:
		if e.code != 404:
			return False
	return True

def padding_oracle(ct, charset):
	guess_pt = ''
	iv = ct[:16]
	ct = ct[16:]
	ct_blocks = block_split(ct)

	for i in range(-1, len(ct_blocks)-1):
			if i >= 0:
				target = ct_blocks[i]
			else:
				target = iv
			guess_block = "\x00"*16
			for j in range(1,len(target)+1):
				padding = "\x00"*(16-j)+chr(j)*j
				for ch in charset:
					if ch == '\x01' and i == len(ct_blocks)-2:
						continue
					guess_block = str_set_chr(guess_block, 16-j, ch)
					new_target = strxor(target, strxor(guess_block, padding))
					if i >= 0:
						ct_blocks[i] = new_target
					else:
						iv = new_target
					sys.stdout.write("TRY %s [%s] => [%s]\r" % ((iv + block_join(ct_blocks[:i+2])).encode('hex'), guess_block.encode('hex'), guess_pt.encode('hex')))
					sys.stdout.flush()
					if padding_oracle_request(iv + block_join(ct_blocks[:i+2])) == True:
						break
			guess_pt += guess_block
	return guess_pt 

def main(argv):
	pt = padding_oracle(ct, charset)
	print "Decrypted::", pt

if __name__ == "__main__":
        main(sys.argv)
