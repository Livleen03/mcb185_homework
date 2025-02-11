for i in range(51, 0, 1):
	print(i)
	for den in range(2, i//2 +1):
		if i % den == 0: print(i)
		else:			 print(i, '*')
		
