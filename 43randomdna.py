# generates DNA sequence in FASTA format
# >sqe-n dna_seq
# random range 50-60

import random

def dna_seq(n, k):
	dna = 'ACGT'
	for k in range(1,k+1):
		if  k >= 1: print('>seq', end='')
		else:       print('error')
		print('-' , end='')
		print(k, end='')
		print()
		for i in range(n+1):
			print(random.choice(dna), end='')
		print()

# Checked, work

dna_seq(55, 1)
dna_seq(60, 2)
