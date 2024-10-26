import sys
import gzip
import mcb185
import itertools

k = int(sys.argv[2])
kcount = {}

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k]
		if kmer not in kcount: kcount[kmer] = 0
		kcount[kmer] += 1


for nts in itertools.product('ACGT', repeat=k):
	kmer = ''.join(nts)
	if kmer not in kcount: print(kmer, 0)

