
import gzip
lengths = []
path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		word = word.split()
		if word[2] != 'CDS': continue
		ini = int(word[3])
		end = int(word[4])
		lengths.append(end - ini + 1) 