# ways to modify the dictionary

d = {}
d = dict()
d = {'dog': 'woof', 'cat': 'meow'}
print(d)
print(d['cat'])
d['pig'] = 'oink'
print(d)

# iteration

for key in d: print( f'{key} says {d[key]}')
for k, v in d.items(): print(k, 'says', v)

# bad example for iteration

## for thing in d.items():print(thing[0], thing[1])

print(d.keys(), d.values(), list(d.values()))