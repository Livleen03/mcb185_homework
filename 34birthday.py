import random
import sys

shared = 0
trials = int(sys.argv[1])
days = int(sys.argv[2])
students = int(sys.argv[3])

for t in range(trials):
	calender = []
	for i in range(days):
		calender.append(0)
	

	for i in range(students):
		bday = random.randint(0, days - 1)
		if calender[bday] == 1:
			shared += 1
			break
			
		calender[bday] += 1
		
print(shared/trials)

