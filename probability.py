import random

def probability():
	errands = 1
	while random.randrange(0,2) == 1:
		errands += 1
	return errands

l = []

for i in range(100):
	l.append(0)

for i in range(100000):
	k=probability()
	l[k] += 1
print(l)

