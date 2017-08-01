import math
n = 600851475143
start = int(math.sqrt(n))
list = range(2, start+1)
list.reverse()
for m in list:
	if n % m == 0:
		prime = True
		for i in range(2, m):
			if m % i == 0:
				prime = False
				break
		if prime:
			largest = m
			break
print largest
