import random
'''
DC       N        A      D
5        80       ?      ?
10		 55       ?      ?
15		 30       ?      ? 
'''

trials = 5
dc = 5
sides = 6
success = 0

def advantage(): 
	roll1 = random.randint(1,20)
	roll2 = random.randint(1,20)
	if roll1 > roll2: return roll1
	return roll2

def disadvantage():
	roll1 = random.randint(1, 20)
	roll2 = random.randint(1,20)
	if roll1 < roll2: return roll1
	return roll1
	
for i in range(trials):
	roll = random.randint(1,20)
	if roll >= dc: success += 1
	print(i, roll)
print(success/trials)

for dc in range(5, 16, 5):
	success = 0 
	for i in range(trials):
		roll = disadvantage()
		if roll >= dc: success += 1
	print(dc, success/trials)

for dc in range(1, 6, 1):
 	nor = 0
 	adv = 0
 	dis = 0
 	for i in range(trials): 
 		r1 = random.randint(1, sides)
 		r2 = random.randint(1, sides)
 		if r1 >= dc: nor += 1
 		if r1 >= dc and r2 >= dc: dis += 1
 		if r1 >= dc or r2 >= dc: adv += 1
 	print(dc, nor/trials, dis/trials, adv/trials)