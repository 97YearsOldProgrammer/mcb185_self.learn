# this is a program for kyle and doolittle hydrophobicity scale of amino acid

def aa_hydro(aa):
	if	 aa == 'I': print('+4.5')
	elif aa == 'V': print('+4.2')
	elif aa == 'L': print('+3.8')
	elif aa == 'F': print('+2.8')
	elif aa == 'C': print('+2.5')
	elif aa == 'M': print('+1.9')
	elif aa == 'A': print('+1.8')
	elif aa == 'G': print('-0.4')
	elif aa == 'T': print('-0.7')
	elif aa == 'S': print('-0.8')
	elif aa == 'W': print('-0.9')
	elif aa == 'Y': print('-1.3')
	elif aa == 'P': print('-1.6')
	elif aa == 'H': print('-3.2')
	elif aa == 'Q': print('-3.5')
	elif aa == 'E': print('-3.5')
	elif aa == 'N': print('-3.5')
	elif aa == 'D': print('-3.5')
	elif aa == 'K': print('-3.9')
	elif aa == 'R': print('-4.0')
	else:			print('error')


# Checked, work

aa_hydro('I')
aa_hydro('K')
aa_hydro('N')
aa_hydro('E')
aa_hydro('B')