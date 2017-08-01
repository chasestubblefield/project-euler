import math
count = 0
term = 1
while True:
	term += 1
	prime = True
	for n in range(2, int(math.sqrt(term)) + 1):
		if term % n == 0:
			prime = False
			break
	if prime:
		count += 1
	if count == 10001:
		break
print term
