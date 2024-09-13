# oligont mp program

def oligont(a, t, c, g):
	if 	 a+t+c+g <= 13: print( (a+t)*2 + (g+c)*4 )
	elif a+t+c+g > 13:  print( 64.9 + 41*(g+c-16.4)/(a+t+g+c))
	else:				print(error)

# test 
# Checked, work

oligont(2,2,2,2)
oligont(4,4,4,4)
oligont(5,5,5,5)