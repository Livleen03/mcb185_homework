import argparse
import mcb185
import math
import sys

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
	

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('--size', type=int, default=20, help='window size')
parser.add_argument('--entropy', type=float, default= 1.4, help='entropy threshold')
parser.add_argument('--lower', action='store_true', help='soft mask')
parser.add_argument('--wrap', type=int, default=80)
arg = parser.parse_args()

	
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	mask = list(seq)
	for i in range(len(seq) - arg.size + 1):
		win = seq[i:i+arg.size]
		if entropy(win) < arg.entropy: 
			for j in range(i, i+arg.size):
				if arg.lower:
					mask[j] = seq[j].lower()
				else: mask[j] = 'N'
				
	print(defline)	
	mask = ''.join(mask)	
	for i in range(0, len(seq),arg.wrap):
		print(mask[i:i+arg.wrap])
