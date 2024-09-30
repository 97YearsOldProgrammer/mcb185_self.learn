import toolbox
import sys

seq  = 'ACGTACGTGGGGGACGTACGTCCCCC'
seqs = list(seq)
w 	 = int(sys.argv[1])
part = seq[0:w]
gc	 = toolbox.g_count(part)
cc	 = toolbox.c_count(part)

for i in range(1, len(seq)-w+1):
	if i + w > len(seq): break
	x = seqs[i - 1]
	if 	 x == ('C'): cc -= 1
	elif x == ('G'): gc -= 1
	y = seqs[i + w -1]
	if 	 y == ('C'): cc += 1
	elif y == ('G'): gc += 1
	comp = (gc + cc)/len(part)
	skew = (gc - cc)/(gc + cc)
	if cc + gc == 0: print(f'{i}\t{comp:.3f}\t0.00')
	else:			 print(f'{i}\t{comp:.3f}\t{skew:.3f}')