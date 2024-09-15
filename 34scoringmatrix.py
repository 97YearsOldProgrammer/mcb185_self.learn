# scoring matrix

alphabet = 'ACGT'
match    = '+1'
mismatch = '-1'

print(' ', end = '')
for letter in alphabet:
	print(letter, end = '')
print()

for i in range(len(alphabet)):
	print(alphabet[i], end=' ')
	for j in range(len(alphabet)):
		if alphabet[i] == alphabet[j]: print(mismatch, end = ' ')
		else:						   print(match, end = ' ')
	print()



