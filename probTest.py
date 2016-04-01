import random

def probability():
	errands = 1
	while random.randrange(0,2) == 1:
		errands += 1
	return errands

def newCustomer():
	if random.randrange(0,5) == 0:
		return True

l = []
k = [0, 0]

for i in range(100):
	l.append(0)


for i in range(100000):
	a = probability()

	l[a] += 1
	if newCustomer():
		k[0] += 1
	else:
		k[1] += 1
print(l)
print()
print(k)
