#!/usr/bin/env python3

import argparse
import mcb185

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20,
	help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
	help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()

#
#
#
#
#
#

import sys
import math
import gzip
import toolbox



x = str(arg.entropy).split('.')
y = int(''.join(x))

lcomplex = []
result	 = []
m        = 0

with gzip.open(arg.file, 'rt') as fp:
	for line in fp:
		if line[0] == '>': 
			continue

		seqs = list(line)
		k	 = -1

		for i in range( len(line) - arg.size +1 ):
			part = line[ i:i+ arg.size ]
			en_f = toolbox.seq_en( part, arg.size )
			en 	 = int( round(en_f, ndigits=1 ) * 10 ) 
			k	+= 1

			if en < y:
				for j in range(arg.size): 

					if m == arg.size: 
						m = 0 
						low_complex = ''.join(seqs)
						lcomplex.append( low_complex )
						break

					m += 1
					seqs[k+m-1] = 'N'

if arg.lower:
	print()
	print(f'>gi|49175990|ref|NC_000913.2| Escherichia coli K12 substr. MG1655, low complexity genome\t')
	print()

	for seq in lcomplex:
		print(seq)