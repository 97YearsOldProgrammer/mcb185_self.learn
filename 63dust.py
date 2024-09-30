import sys
import math
import gzip
import toolbox

file = sys.argv[1]
w 	 = int(sys.argv[2])
lim_e= sys.argv[3]

# turning input limit into integral

x = str(lim_e).split('.')
y = int(''.join(x))

lcomplex = []
result	 = []
m        = 0

with gzip.open(file, 'rt') as fp:
	for line in fp:
		if line[0] == '>': 
			continue

		seqs = list(line)
		k	 = -1

		for i in range(len(line) -w +1):
			part = line[i:i+w]
			en_f = toolbox.seq_en(part, w)
			en 	 = int(round(en_f, ndigits=1 ) * 10) 
			k	+= 1

			if en < y:
				for j in range(w): 

					if m == w: 
						m = 0 
						low_complex = ''.join(seqs)
						lcomplex.append(low_complex)
						break

					m += 1
					seqs[k+m-1] = 'N'

print(f'>gi|49175990|ref|NC_000913.2| Escherichia coli K12 substr. MG1655, low complexity genome\t')
print()

for seq in lcomplex:
	print(seq)

			

			







					


		
