import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

def dtc(I, N):
	d = 0
	for i, n in zip(I, N):
		d += abs(i - n)
	return d

min_dist = 255

with open(colorfile) as fp:
	for line in fp:
		f = line.split()
		name = f[0]
		
		color_values = []
		for c in f[2].split(','):
    			color_values.append(int(c))
    	x = [R, G, B]		
		dist = dtc(x, color_values)
		if dist < min_dist: 
			min_dist = dist
			chosen_color = name
		
print(chosen_color)
	
	


'''
def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d
'''	
	
'''
def minimum(vals):
2       mini = vals[0]
3       for val in vals[1:]:
4           if val < mini: mini = val
5       return mini


def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d
	
	limit = 6
for r in range(limit):
	for g in range(limit):
		for b in range(limit):
			c1 = best_color(r, g, b)
			c2 = optimal_color(r, g, b)
			c3 = great_color(r, g, b)
			if c1 == c2 and c1 == c3
'''