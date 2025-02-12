t = 1, 2	# this is a tuple
print(t)
print(type(t))

person = 'Steve', 21, 57891.50 # name, age, yearly income
print(person)

def midpoint(x1, y1, x2, y2):
	x = (x1 + x2) / 2
	y = (y1 + y2) / 2
	return x, y
print(midpoint(5, 7, 3, 8))

'''
while True:
	print('hello')
'''

i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 3: break
	
i = 0	
while i < 3:
	i = i + 1
	print('hey', i)
	
i = 1
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)

for i in range(1, 10, 3):
	print(i)
	
for i in range(0, 5):
	print(i)

for i in range(5):
	print(i)
	
for i in range(7):
    if i % 2 == 0: print(i, 'is even')
    else:          print(i, 'is odd')

# practice problems 

def triangular(n): 						#triangular
	total = 0
	for i in range(1, n + 1):
		total = total + i
	return total
print(triangular(10))


def factorial(n):						#factorial
	total = 1
	for i in range(1, n + 1):
		total = total * i
	return total
print(factorial(0))

import math
def poisson(n, k):						# poisson probability
	prob = (n**k * math.e**-n) / factorial(k)
	return prob
print(poisson(4, 8))
	
def nchoosek(n, k):   #n chooses k (could just write return and no number)
	number = factorial(n) / (factorial(k) * factorial(n - k))
	return number
print(nchoosek(5, 9))

def euler(limit):                   # euler's number
	e = 0 
	for n in range(limit):
		e = e + 1 / factorial(n)
	return e
print(euler(200))

def is_prime(n):						# is number prime
	for den in range(2, n//2 +1):
		if n % den == 0: return False
	return True 
print(is_prime(2))

def nilakantha(limit):					# nilakantha series to estimate pi
	pi = 3
	for i in range(1, limit+1):
		n = 2 * i
		d = n * (n + 1) * (n + 2)
		if i % 2 == 0: pi = pi - 4 / d
		else: 			pi = pi + 4 / d
	return pi
print(nilakantha(300))


# random numbers 
import random 

for i in range(5):
	print(random.random())
	
for i in range(3):
	print(random.randint(1, 6))
	
# More practice                    

import random                           # Monty Pi-thon
'''
countin = 0
countout = 0

while True:
	x = random.random()
	y = random.random()
	dist = (x ** 2 + y ** 2) ** (0.5)
	
	if dist <= 1: countin += 1
	if dist > 1: countout += 1
	print( 4 * (countin) / (countin + countout))
'''
                                            # D&D 3d6 
n = 10000								
total = 0 
for i in range(n):
	r1 = random.randint(1, 6)
	r2 = random.randint(1, 6)
	r3 = random.randint(1, 6)
	total += r1 + r2 + r3
print(total / n) 

n = 10000									# D&D 3d6r1 
total = 0 
for i in range(n):
	r1 = random.randint(1, 6)
	if r1 == 1: 
		r1 = random.randint(1, 6)
	r2 = random.randint(1, 6)
	if r2 == 1: 
		r2 = random.randint(1, 6)
	r3 = random.randint(1, 6)
	if r3 == 1: 
		r3 = random.randint(1, 6)
	total += r1 + r2 + r3
print(total / n) 

n = 10000                                   # D&D 3d6x2
total = 0 
for i in range(n):
	for j in range(3):
		d1 = random.randint(1,6)
		d2 = random.randint(1,6)
		if d1 > d2:
			max_number = d1
		else: 
			max_number = d2
		total += max_number     # += is same as total = max_number + total
print(total / n)

n = 10											# D&D 4D6d1
total = 0
for i in range(n):
		d1 = random.randint(1,6)
		d2 = random.randint(1,6)
		d3 = random.randint(1,6)
		d4 = random.randint(1,6)
		print(d1, d2, d3, d4)	
		if d1 < d2 and d1 < d3 and d1 < d4:
			total += d2 + d3 + d4
		elif d2 < d1 and d2 < d3 and d2 < d4:
			total += d1 + d3 + d4
		elif d3 < d1 and d3 < d2 and d3 < d4:
			total += d2 + d1 + d4
		elif d4 < d1 and d4 < d2 and d4 < d3:
			total += d2 + d1 + d3
print(total/n)
									



	
	

	






	
	