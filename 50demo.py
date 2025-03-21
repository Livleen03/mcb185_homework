#sets

s = {'A', 'C', 'G'}
print(s)

s.add('A')   #does not change set since adding the same element
print(s)

# print(s[2]) will give error since set doesn't have order


#dictionaries 

d = {}        #both do same thing
d = dict()

d = {'dog': 'woof', 'cat': 'meow'}
print(d)

print(d['cat'])

d['pig'] = 'oink'
print(d)

d['cat'] = 'mew'
print(d)

del d['cat']
print(d)

if 'dog' in d: print(d['dog'])

#iteration

for key in d: print(f'{key} says {d[key]}')

for k, v in d.items(): print(k, 'says', v)

print(d.keys(), d.values(), list(d.values()))


import itertools
for nts in itertools.product('ACGT', repeat=2):
    print(nts)



