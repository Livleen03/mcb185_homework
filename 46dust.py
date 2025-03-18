import mcb185
import math
import sys

	
w = int(sys.argv[2])
ent_thres = float(sys.argv[3])
lower = False

def entropy(win):
	a = win.count('A') / len(win)
	c = win.count('C') / len(win)
	g = win.count('G') / len(win)
	t = win.count('T') / len(win)
	h = 0
	if a != 0: h-= a*(math.log2(a))
	if c != 0: h-= c*(math.log2(c))
	if g != 0: h-= g*(math.log2(g))
	if t != 0: h-= t*(math.log2(t))
	return h

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	mask = list(seq)
	for i in range(len(seq) - w + 1):
		win = seq[i:i+w]
		if entropy(win) < ent_thres: 
			for j in range(i, i+w):
				if lower:
					mask[j] = seq[j].lower()
				else: mask[j] = 'N'
				
	print(defline)	
	mask = ''.join(mask)	
	for i in range(0, len(seq),60):
		print(mask[i:i+60])
		
		
		
		
		
		
		
		
		