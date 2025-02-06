# 10demo.py by Livleen Grewal

import math 

print ('hello again') # greeting
print(1.5e-2)
print(1+1)
print(1-1)
print(2 * 2)
print(1 / 2)
print (2 ** 3)
print (5 // 2)
print(5 % 2)
print(5 * (2+1))
print(pow(2, 3))
print(math.pow(2, 3))
print(2**0.5)
print(math.sqrt(2))
print(math.log(2))
#print (1 / 0)				# divide by zero error
#print(math.log(0))			# math domain error
#print(math.sqrt(-1))		# math domain error

print(0.1 * 1)
print(0.1 *3)

a = 3						# side of triangle 
b = 4						# side of triangle 
c = math.sqrt (a**2 + b**2)	# hypotenuse 
print (c)

print(type(a), type (b), type(c))
print(type(a), type(b), type(c), sep=', ', end= '!\n')

def pythagoras(a, b):
		c = math.sqrt(a**2 + b**2)
		return c 

hyp = pythagoras(3, 4)
print(hyp)

def pythagoras(a, b): 
		return math.sqrt(a**2 + b**2)
		
print(pythagoras(3, 4))

def pythagoras(a, b): return math.sqrt(a**2 + b**2)

def circle_area(r): return math.pi * r**2 
print(circle_area(2))

def rectangle_area(w, h): return w * h
def triangle_area(w, h): return rectangle_area(w, h) / 2



#Practice

def f_to_c(f):					# convert F to C 
	return ((f-32) * (5/9))
print('temp', f_to_c(98))

def c_to_f(c):					# convert C to F 
	return ((c * (9/5)) + 32)
print(c_to_f(10))

def mph_to_kph(m):              # convert mph to kph 
	return m / 0.62
print(mph_to_kph(12))

def kph_to_mph(k):              # convert kph to mph 
	return (k * 1.609)
print(kph_to_mph(12000))

def dna_conc(od260):            # DNA concentration from OD260
	return (od260 * 50)
print(dna_conc(30))

def arth_mean(a, b, c): 	     # arithmetic mean of 3 numbers 
	return ((a + b + c) / 3)
print(arth_mean(4, 5, 8))

def geo_mean(a, b, c):            # geometric mean of 3 numbers
	return ((a * b * c) ** (1/3))
print(geo_mean(4, 5, 8))

def harmonic_mean(a, b, c): 	  # harmonic mean of 3 numbers
	n = 3
	sum = (1/a) + (1/b) + (1/c)
	return n/sum
print(harmonic_mean(4, 5, 8))

def dist2(x1, y1, x2, y2):       # distance between 2 points in graph
	x_dist = x2 - x1
	y_dist = y2 - y1
	return math.sqrt(x_dist ** 2 + y_dist ** 2)
print(dist2(0, 0, 3, 4))



s = 'hello world'                # strings
print(s, type(s))

# Conditionals 
a = 2
b = 2
if a == b:
		print('a equals b')
		
if a == b:
	print('a equals b')
	print(a, b)
	
if a == b:
	print('a equals b')
print(a, b)

def is_even(x): 
		if x % 2 == 0: return True
		return False

print(is_even(2))
print(is_even(3))

# Boolean 

c = a == b
print(c)
print(type(c))

# if-elif-else

if a < b:
		print('a < b')
elif a > b: 
		print('a > b')
else: 	
		print('a == b')
		
if	a < b:  print('a < b')
elif a > b: print('a > b')
else:		print('a == b')

if	a < b:	 print('a < b')
elif a<= b:  print('a <= b')
elif a == b: print('this will never print!')

if a < b or a > b: print('all things being equal, a and b ar not')
if a < b and a > b: print('you are livivng in a stragne world')
if not False: print(True)

# Floating Point Warning 

a = 0.3
b = 0.1 * 3
if	  a < b: print('a < b')
elif  a > b: print('a > b')
else: 		 print('a == b')

print(abs(a - b)) # 5.551115123125783e-17
if abs(a - b) < 2e-9: print('close enough')

if math.isclose(a, b): print('close enough')

# String Comaprison 

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('A < a')

# Mismatched Type Error

			#error message shown 

# None Type

def silly(m, x, b): 
		y = m * x + b
print(silly(2, 3, 4))


# More Practice 

def is_integar(i):              # if number is an integar
	return i % 1 == 0
print(is_integar(2))
print(is_integar(2.3))

def if_valid_probability(p):       # valid probability
		return 0 <= p <= 1
print(if_valid_probability(0.4))
print(if_valid_probability(2))
print(if_valid_probability(0.5))

def dna_weight(w):							# molecular weight of DNA
	if w == 'A':   return '331.2 g/mol'
	elif w == 'G': return '347.2 g/mol'
	elif w == 'C': return '307.2 g/mol'
	elif w == 'T': return '322.2 g/mol'
	else: return 'None'
print(dna_weight('A'))
print(dna_weight('F'))
print(dna_weight('C'))

def dna_complement(c): 						# DNA complement letter
	if c == 'A':   return 'T'
	elif c == 'T': return 'A'
	elif c == 'G': return 'C'
	elif c == 'C': return 'G'
	else:          return 'None'
print(dna_complement('A'))
print(dna_complement('B'))


# Even More Practice 

def max3(n1, n2, n3):                         # max of 3 numbers
	if n1 > n2 and n1 > n3:   return n1
	elif n2 > n1 and n2 > n3: return n2
	else:                     return n3
print(max3(5, 3, 10))
print(max3(4, 3, 1))

def con_matrix(TP, TN, FP, FN):
	sensitivity = TP / (TP + FN) 
	specificity = TN / (TN + FP)
	score = 2 * ((sensitivity * specificity) / (sensitivity + specificity))
	return sensitivity, specificity, score
print(con_matrix(3,4,6,2))

def shannon_entropy(A, C, G, T):			# shannon entropy
	total = A + C + G + T
	PA = A / total
	PC = C / total
	PG = G / total
	PT = T / total 
	entropy_A = PA * math.log2(PA) if PA > 0 else 0 
	entropy_C = PC * math.log2(PC) if PC > 0 else 0 
	entropy_G = PG * math.log2(PG) if PG > 0 else 0 
	entropy_T = PT * math.log2(PT) if PT > 0 else 0 
	entropy_total = -1 * (entropy_A + entropy_C + entropy_G + entropy_T)
	return entropy_total
print(shannon_entropy(10,20,30,40))
print(shannon_entropy(0,20,30,40))





	

