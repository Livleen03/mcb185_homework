import math

# strings

s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

print('hey "dude" don\'t tell me what to do')

s = 'hello' + 'world'
print(s)

print(s.upper())
print(s)

print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))

print(f'{math.pi}')
print(f'{math.pi:.3f}')
print(f'{1e6 * math.pi:e}')
print(f'{"hello world":>20}')
print(f'{"hello world":.>20}')
print(f'{20:<10} {10}')

print('{} {:.3f}'.format('str.format', math.pi))

print('%s %.3f' % ('printf', math.pi))


# indexes

seq = 'GAATTC'
print(seq[0], seq[1])

print(seq[-1])

for nt in seq:
	print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])
	
# slices

s = 'ABCDEFGHIJ'
print(s[0:5])

print(s[0:8:2])

print(s[0:5], s[:5])				# both ABCDE
print(s[5:len(s)], s[5:])			# both FGHIJ

print(s, s[::], s[::1], s[::-1])

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
	codon = dna[i:i+3]
	print(i, codon)
	
#tuples

tax = ('Homo', 'sapiens', 9606)		# construct tuple 
print(tax)							# parenthesis!

'''
s[0] = 'C'		# get error since cant chance content of tuples and string
tan[0] = 'human'
'''
print(tax[0])			# index
print(tax[::-1])		# slice

# enumerate() and zip()

nts = 'ACGT'								#enumerate
for i in range(len(nts)):
	print(i, nts[i])

for i, nt in enumerate(nts):
	print(i, nt)
											# zip

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])
	
for nt, name in zip(nts, names):
	print(nt, name)
	
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)
	
#Lists

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

# To make a copy, use list.copy()

items = list()						#list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)
									# split() and join()

text = 'good day           to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

s = '_'.join(aas)
print(s)
s = ''.join(aas)
print(s)

if 'A' in alph: print('yay')
if 'a' in alph: print('no')

'''
print('index G?', alph.index('G'))
print('index Z?', alph.index('Z'))
'''

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))

# Practice Problems

def minimum(vals):					#minimum()
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini
print(minimum([3, 7, 4, 6]))


def minmax(vals):					#minmax()
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		elif val > maxi: maxi = val 
	return mini, maxi
print(minmax([3, 7, 4, 6]))	


def mean(vals):						#mean()
	total = 0
	for val in vals: total += val 
	mean_number = total / len(vals)
	return mean_number
print(mean([10, 8]))

import math						# entropy()
def entropy(probs):
	h = 0
	for p in probs:  
		if p > 0:
			h -= p * math.log2(p)
	if sum(probs) != 1.0 : return 'error, sum of probs not 1'
	else: return h 
print(entropy([0.2, 0.3, 0.5]))
print(entropy([1, 0.3, 0.5]))		
print(entropy([0, 0.5, 0.5]))	

def dkl(P, Q):						# Kullback-Leibler distance
    d = 0
    for p, q in zip(P, Q):
        d += p * math.log2(p/q)
    return d
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.2)
print(dkl(p1, p2))

# Command line data

import sys
print(sys.argv)

# converting types

i = int('42')
x = float('0.61803')
print(i * x)

# pairwise comparison


# assessment example

# 1
# A-B-C-D-E to -C-
print('-'.join(list('ABCDE'))[3:6])

#2 
# in 32stats.py

#3

seq = 'ATGCTGTAA'
for i in range(0, 7, 1):
	position = (i+1)
	frame = (i % 3) + 1
	codon = seq[i:i+3]
	print(position, frame, codon, sep='\t')
	
