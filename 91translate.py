import argparse
import gzip
import mcb185
import toolbox

parser = argparse.ArgumentParser(description='mRNA tranlator.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-m', '--min', type=int, default=100,
	help='minimum protein length [%(default)i]')
parser.add_argument('-a', '--anti', action='store_true',
	help='also examine the anti-parallel strand')
arg = parser.parse_args()

for defline, seq in mcb185.read_fasta(arg.file):

	for i in range(0, len(seq), 3):
		codon = seq[i:i+3]

		if codon == 'ATG':
			seq = seq[i: len(seq)]

			if len(seq) >= arg.min:

				print(f'{defline}\n{toolbox.translate_pro(seq)}')
				continue


if arg.anti: 

	print(f'\nThis is anti strand\n')
	for defline, seq in mcb185.read_fasta(arg.file):
		
		seq = toolbox.revcomp(seq)

		for i in range(0, len(seq), 3):

			codon = seq[i:i+3]

			if codon == 'ATG':

				seq = seq[i: len(seq)]

				if len(seq) >= arg.min:

					print(f'{defline}\n{toolbox.translate_pro(seq)}')
					continue



