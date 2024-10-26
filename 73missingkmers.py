import sys
import gzip
import mcb185
import itertools
import toolbox

# creating a value for k 

kmax = int(sys.argv[2])
x    = 0
n    = 0
kcount = {}


""" making kmer output library """

k = 0

for i in range(kmax):
	k += 1

	for defline, seq in mcb185.read_fasta(sys.argv[1]):
		for i in range(len(seq) -k +1):
			kmer = seq[i:i+k]
			if kmer not in kcount: kcount[kmer] = 0
			kcount[kmer] += 1

""" making reverse strand check """

y = 0

for i in range(kmax):
	y += 1

	for defline, seq in mcb185.read_fasta(sys.argv[1]):
		for i in range(len(seq) -y +1):
			kmer  = seq[i:i+y]
			rkmer = toolbox.revcomp(kmer)
			if rkmer not in kcount: kcount[rkmer] = 0
			kcount[rkmer] += 1

""" sorting missing kmer with given intertool """

for j in range(kmax):
	x += 1

	for nts in itertools.product('ACGT', repeat=x):
		kmer = ''.join(nts)

## if we want see the exact output
		if kmer not in kcount: print(f'{kmer}\t0\t{x}')
		
## if we want to run the wc to see how many output we have
##		if kmer not in kcount: n += 1

## print(n)




