import time
import sequence 

t0 = time.time()

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10
for i in range(len(seq) -w +1):
	s = seq[i:i+w]
	print(i, s, sequence.gc_comp(s), sequence.gc_skew(s))	
t1 = time.time()
print(t1-t0)
	
	
