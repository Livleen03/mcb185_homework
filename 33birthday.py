import random
import sys

shared = 0
trials = int(sys.argv[1])
days = int(sys.argv[2])
students = int(sys.argv[3])

for t in range(trials):
	peeps = []
	for i in range(students):
		bday = random.randint(0, 364)
		if bday in peeps:
			shared += 1
			break
		peeps.append(bday)
		
print(shared / trials)






