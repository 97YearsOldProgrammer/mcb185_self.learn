import re
import sys
import mcb185


for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if 'DKTGT' in seq: print(defline)


#for defline, seq in mcb185.read_fasta(sys.argv[1]):
#    if re.search('C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H', seq): print(defline)
#
#pat = '(C.{2.4}C.{3}[LIVMFYWC].{8}H.{3,5}H)'
#for defline, seq in mcb185.read_fasta(sys.argv[1]):
#	m = re.search(pat, seq)
#	if m: print(m.group(1)) 