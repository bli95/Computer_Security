#!/usr/bin/env python

import sys

def main():
	if len(sys.argv) != 3:
		print 'Not the right number of argument. You fail. Tried again.'
		sys.exit(1)

	with open(sys.argv[1]) as file:
		input = file.read().strip()

	# WHA algorithm
	inStr = bytearray(input)
	mask = 0x3FFFFFFF
	outHash = 0
	for byte in inStr:
		intermediate_val = ((byte ^ 0xCC) << 24) | ((byte ^ 0x33) << 16) | ((byte ^ 0xAA) << 8) | (byte ^ 0x55)
		outHash = (outHash & mask) + (intermediate_val & mask)
	
	with open(sys.argv[2], 'w') as file:
		file.write("%x" % outHash)

if __name__ == "__main__":
	main()