import math 


def char_to_prob(c):
	pqv = ord(c) - 33
	prob = 10 ** (-pqv/10)
	return prob
print(char_to_prob('B'))
	
	
def prob_to_char(p):
	if not 0 < p < 1: return None 
	pqv = -(math.log10(p) * 10)
	if pqv < 0 or pqv > 93: return None
	char = int(pqv) + 33
	return chr(char)
print(prob_to_char(0.001))
	


#p = 1 * 10 ** -3.3
#print(p)
#pqv = -int(math.log10(p) * 10)
#symbol = chr(pqv+33)
#print(symbol)

#c = 'K' 
#pqv = ord(c) - 33
#print(10**(-pqv/10))


# if probabilty less than this number than illegal
# 	if p < 1e-9: return None 

# def prob_to_char(p):