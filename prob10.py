import math

def is_prime(n):
	prime = True
	for m in range(2, int(math.sqrt(n))):
		if n % m == 0:
			prime = False
			break
	if math.sqrt(n) == int(math.sqrt(n)):
		prime = False
	return prime

sum = 0
curr = 2
while curr < 2000000:
	if is_prime(curr):
		sum += curr
	curr += 1
print sum
