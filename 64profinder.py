# input multi-FASTA of DNA
# outpit multi-fasta of proteins
# six-frame translation
# 100 amino acids long at least 

# format
# proteins start with 'M' end with '*'
# unique identifiers with defline

import sys
import toolbox
import gzip

file   = sys.argv[1]
length = sys.argv[2]
l 	   = int(length)

seqs = []

with gzip.open(file, 'rt') as fp:
	for line in fp:
		if line[0] == '>':
			words 	  = line.split()
			defline   = words[0]
			firstline = words[1:6]
			continue
		seqs.append(line)

# forward sequence

seq = ''.join(seqs)
seq1 = seq[1:len(seq)] 
seq2 = seq[2:len(seq)]

proteins  = toolbox.translate(seq)
proteins1 = toolbox.translate(seq1)
proteins2 = toolbox.translate(seq2)

# reverse sequence

rseq  = toolbox.revcomp(seq)
rseq1 = toolbox.revcomp(seq1)
rseq2 = toolbox.revcomp(seq2)

rproteins = toolbox.translate(rseq)
rproteins1= toolbox.translate(rseq1)
rproteins2= toolbox.translate(rseq2)

# function for translation and data collection

pts = []
def extract_pro(pro):

	for protein in pro:
		x  = pro.find('M')
		y  = pro.find('*')
		if x == -1 or y == -1: break

		prot = []
		if x < y: prot = pro[x:y+1]

		if x > y: pro = pro[x:]
		else:     pro = pro[y+1:]

		if len(prot) >= l: pts.append(prot)

	return pts

def output_pro(pros):

	j = 0
	for pt in pros:
		print(f' {defline}-prot-{j}\n{pt}')
		j += 1

# start output formatting here

headline = ' '.join(firstline)
print(headline)
print()

print(f'This is frame1\n')
extract_pro(proteins)
output_pro(pts)
print()

print(f'This is frame2\n')
extract_pro(proteins1)
output_pro(pts)
print()

print(f'This is frame3\n')
extract_pro(proteins2)
output_pro(pts)
print()

print(f'This is reverse frame1\n')
extract_pro(rproteins)
output_pro(pts)
print()

print(f'This is reverse frame2\n')
extract_pro(rproteins1)
output_pro(pts)
print()

print(f'This is reverse frame3\n')
extract_pro(rproteins2)
output_pro(pts)
