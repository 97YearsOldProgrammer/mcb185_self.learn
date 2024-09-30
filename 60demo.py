import sys
import mcb185

""" ways to read a FASTA file"""

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline[:30], seq[:40], len(seq))

""" stepping through FASTA file"""
"""
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name	 = defwords[0]
	gc = 0
	for nt in seq:	
		if nt == 'C' or nt == 'G': gc += 1
		rint(name, gc/len(seq))

A = 0
C = 0
G = 0
T = 0
N = 0
for nt in seq:
	if   nt == 'A': A += 1
	elif nt == 'C': C += 1
	elif nt == 'G': G += 1
	elif nt == 'T': T += 1
	else:			N += 1"""