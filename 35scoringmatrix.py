import sys 

list_seq_1 = sys.argv[1]
list_seq_2 = sys.argv[1]
matches = int(sys.argv[2])
mismatch = int(sys.argv[3])

print('  '+'  '.join(list_seq_2))

for i in range(0, len(list_seq_1)):
	print(list_seq_1[i], end=" ")	
	for j in range(0, len(list_seq_2)):			
		if list_seq_1[i] == list_seq_2[j]:
			print(f'{matches:>2}', end=" ")
		else:
			print(f'{mismatch:>2}', end=" ")
			
	print()
'''
import sys 

seq_1 = sys.argv[1]
seq_2 = sys.argv[1]
matches = int(sys.argv[2])
mismatch = int(sys.argv[3])

print(" "+" ".join(seq_2))

for i in range(0, len(seq_1)):
	print(seq_1[i], end=" ")	
	for j in range(0, len(seq_2)):			
		if seq_1[i] == seq_2[j]:
			print(f"{matches:+}", end=" ")
		else:
			print(f"{mismatch:+}", end=" ")	
	print()
	

import random
import sys

len(list) = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

for i in range(0, len(list)):
	for j in range(0, len(list)):
	
python3 35scoringmatrix.py ACGT +1 -1


import sys 

list_seq = sys.argv[1]
matches = int(sys.argv[2])
mismatch = int(sys.argv[3])

for i in range(0, len(list_seq)):
	for j in range(0, len(list_seq)):
		list_seq_combined = (list_seq[i], list_seq[j])
					
		if list_seq[i] == list_seq[j]:
			print((''.join(list_seq_combined)), matches)
		else:
			print((''.join(list_seq_combined)), mismatch)
			
'''






