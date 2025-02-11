f1 = 0 
f2 = 1
print (f1)
print (f2)

for i in range(0,8):
	fn = f1 + f2  # this in sum 
	f1 = f2   # store f2 as f1 for next number
	f2 = fn  # storing fn as f2 for next number  
	print(fn)
'''
f1 + f2 = fn
1 + 2 = 3

f1 + f2 = fn 
2 + 3 = 5
'''