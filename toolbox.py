import math

def transcribe(dna):
	return dna.replace('T', 'U')

def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if 	 nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:			rc.append('N')
	return ''.join(rc)

def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]

	# this is for Met protein
		if 	 codon == 'ATG': aas.append('M')

	# this is for Phe protein
		elif codon == 'TTT': aas.append('F')
		elif codon == 'TTC': aas.append('F')

	# this is for Leu protein
		elif codon == 'TTA': aas.append('L')
		elif codon == 'TTG': aas.append('L')

		elif codon == 'CTT': aas.append('L')
		elif codon == 'CTC': aas.append('L')
		elif codon == 'CTA': aas.append('L')
		elif codon == 'CTG': aas.append('L')

	# this is for Ile protein
		elif codon == 'ATT': aas.append('I')
		elif codon == 'ATC': aas.append('I')
		elif codon == 'ATA': aas.append('I')

	# this is for Val protein
		elif codon == 'GTT': aas.append('V')
		elif codon == 'GTC': aas.append('V')
		elif codon == 'GTA': aas.append('V')
		elif codon == 'GTG': aas.append('V')

	# this is the Ser protein
		elif codon == 'TCT': aas.append('S')
		elif codon == 'TCC': aas.append('S')
		elif codon == 'TCA': aas.append('S')
		elif codon == 'TCG': aas.append('S')

		elif codon == 'AGT': aas.append('S')
		elif codon == 'AGC': aas.append('S')

	# this is the Pro protein
		elif codon == 'CCT': aas.append('P')
		elif codon == 'CCC': aas.append('P')
		elif codon == 'CCA': aas.append('P')
		elif codon == 'CCG': aas.append('P')

	# this is the Thr protein
		elif codon == 'ACT': aas.append('T')
		elif codon == 'ACC': aas.append('T')
		elif codon == 'ACA': aas.append('T')
		elif codon == 'ACG': aas.append('T')

	# this is the Ala protein
		elif codon == 'GCT': aas.append('A')
		elif codon == 'GCC': aas.append('A')
		elif codon == 'GCA': aas.append('A')
		elif codon == 'GCG': aas.append('A')

	# this is the Tyr protein
		elif codon == 'TAT': aas.append('Y')
		elif codon == 'TAC': aas.append('Y')

	# this is the His protein
		elif codon == 'CAT': aas.append('H')
		elif codon == 'CAC': aas.append('H')

	# this is the Gln protein
		elif codon == 'CAA': aas.append('Q')
		elif codon == 'CAG': aas.append('Q')

	# this is the Asn protein
		elif codon == 'AAT': aas.append('N')
		elif codon == 'AAC': aas.append('N')

	# this is the Lys protein
		elif codon == 'AAA': aas.append('K')
		elif codon == 'AAG': aas.append('K')

	# this is the Asp protein
		elif codon == 'GAT': aas.append('D')
		elif codon == 'GAC': aas.append('D')

	# this is the Glu protein
		elif codon == 'GAA': aas.append('E')
		elif codon == 'GAG': aas.append('E')

	# this is the Cys protein
		elif codon == 'TGT': aas.append('C')
		elif codon == 'TGC': aas.append('C')

	# this is for Trp protein
		elif codon == 'TGG': aas.append('W')

	# this is for Arg protein
		elif codon == 'CGT': aas.append('R')
		elif codon == 'CGC': aas.append('R')
		elif codon == 'CGA': aas.append('R')
		elif codon == 'CGG': aas.append('R')

	# this is for Ser protein
		elif codon == 'AGT': aas.append('S')
		elif codon == 'AGC': aas.append('S')

	# this is for Arg protein
		elif codon == 'AGA': aas.append('R')
		elif codon == 'AGG': aas.append('R')

	# this is for Gly protein
		elif codon == 'GGT': aas.append('G')
		elif codon == 'GGA': aas.append('G')
		elif codon == 'GGC': aas.append('G')
		elif codon == 'GGG': aas.append('G')

	# this is for stopping codon
		elif codon == 'TAA': aas.append('*')
		elif codon == 'TAG': aas.append('*')
		elif codon == 'TGA': aas.append('*')

		else:				 aas.append('X')
	return ''.join(aas)

def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)

def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)

def c_count(seq):
	return seq.count('C')

def g_count(seq):
	return seq.count('G')

# calculating Shannon entropy of DNA sequences

def seq_en(seq, x):
	a = seq.count('A')
	if a != 0: ha = - a/x * math.log2( a/x )
	else: 	   ha = 0
	t = seq.count('T')
	if t != 0: ht = - t/x * math.log2( t/x )
	else: 	   ht = 0
	c = seq.count('C')
	if c != 0: hc = - c/x * math.log2( c/x )
	else:	   hc = 0	
	g = seq.count('G')
	if g != 0: hg = - g/x * math.log2( g/x )
	else:	   hg = 0
	se = ha + ht + hc + hg
	return se

# dictionary for translating DNA sequence from Dr.ian

gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}

def translate_pro(seq):
	pro = []
	for i in range(0, len(seq), 3):
		codon = seq[i:i+3]
		if codon in gcode: aa = gcode[codon]
		else:              aa = 'X'
		pro.append(aa)
	return ''.join(pro)

# dictionary for calculating hydropathy from Dr.ian

kdh = {
	'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5,
	'M':  1.9, 'A':  1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8,
	'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5,
	'Q': -3.5, 'D': -3.5, 'K': -3.9, 'N': -3.5, 'R': -4.5,
}

def hydropathy(seq):
	s = 0
	for aa in seq:
		s += kdh[aa]
	return s / len(seq)

# based on unit 8 data part, modified verion of 22oligotem.py
# not sure if it meet thre requirement or not

def oligont(string):
	d = {'A': 0, 'C': 0, 'G': 0, 'T': 0, '*': 0}
	for nt in string:

		if nt in d: d[nt]  += 1
		else: 		d['*'] += 1

	count = list(d.values())
	total = sum(d.values())

	if total <= 13:   return (d['A']+ d['T'] ) *2 + ( d['G'] + d['C'] ) *4 
	elif total > 13:  return (64.9 + 41*( d['G'] + d['C'] -16.4)/(total))

# typical structure for reading CSV file
# This is non-universal function for every CSV file, display and learning purpose
# from Dr.korf at unit 8

""" def read_catalog(filepath):
	catalog = []
	with open(filepath) as fp:
		for line in fp:
			if line.startswith('#'): continue
			name, length, seq, desc = line.rstrip().split(',')
			record = {
				'Name': name,
				'Length': length,
				'Sequence': seq,
				'Description': desc
			}
			catalog.append(record)
	return catalog """

# for modification to test

def read_fasta(filename):
	"""iteratively read records from a FASTA file"""
	if   filename == '-':          fp = sys.stdin
	elif filename.endswith('.gz'): fp = gzip.open(filename, 'rt')
	else:                          fp = open(filename)
	name = None
	seqs = []
	while True:
		line = fp.readline()
		if line == '': break
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				yield(name, ''.join(seqs))
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)

	yield(name, ''.join(seqs))
	fp.close()
