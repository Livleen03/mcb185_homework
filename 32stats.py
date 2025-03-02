
import sys
import math

def stats():
	vals = []
	
	for arg in sys.argv[1:]:
		f = float(arg)
		vals.append(f)
	
	length = 'length=', len(vals)


	mini = vals[0]
	maxi = vals[0]					             #minmax()
	for val in vals:    
		if val < mini: mini = val
		if val > maxi: maxi = val
	minmax = 'min and max =', mini, maxi
	
											#mean()
	mean = 0	
	total = 0
	for val in vals: 
		total += val 
	mean = 'mean=', total / len(vals)
	
	stdev = 0
	num = 0
	for val in vals:
		num += (val - total / len(vals)) ** 2
		stdev = 'stdev=', math.sqrt(num / (len(vals) - 1))

	median = 0 
	vals.sort()
	n = len(vals)
	if n % 2 == 0:
		median = 'median=', (vals[n // 2 - 1] + vals[n // 2 ]) / 2
	else: 
		median = 'median=', vals(n // 2)	
	
	n50sum = 0
	vals.sort()
	for val in vals:
		n50sum += val 
	n50half = 0
	n50idx = -1
	while (n50half < n50sum / 2):
		n50idx += 1
		n50half += vals[n50idx]
	
	return length, minmax, mean, stdev, median, 'N50=', vals[n50idx]

print(stats())
