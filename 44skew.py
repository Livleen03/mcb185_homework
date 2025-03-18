import sequence
import sys
import mcb185

w = int(sys.argv[2])
g = 0
c = 0
n = 0

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	c = seq[0:w].count('C')
	g = seq[0:w].count('G')
	
	if g+c != 0:
		print(n, sequence.gc_comp(seq[0:w]), sequence.gc_skew(seq[0:w]))
	else:
		print(n,0,0)

	for i in range(w, len(seq) + 1):
		if seq[i : i+1] == 'C':
			c +=1 
		if seq[i : i+1] == 'G':
			g += 1

		if seq[i - w: i-w+1] == 'C':
			c -= 1
		if seq[i - w: i-w+1] == 'G':
			g -= 1

		n += 1
		if g+c != 0:
			print(n, sequence.gc_comp(seq[0:w]), sequence.gc_skew(seq[0:w])) 
		else: 
			print(n, 0, 0)
print()