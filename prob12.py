import math

def num_divisors(n):
	num = 0
	for i in range(1, int(math.sqrt(n))):
		if n % i == 0:
			num += 2
	if math.sqrt(n) == int(math.sqrt(n)):
		num += 1
	return num

tri = 1
count = 1
while num_divisors(tri) <= 500:
	count += 1
	tri += count

print tri
