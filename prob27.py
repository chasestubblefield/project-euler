from euler_util import is_prime

maxnum, maxa, maxb = (0, 0, 0)
for a in range(-999, 1000):
	for b in range(-999, 1000):
		num = 0
		n = 0
		while is_prime(n**2 + a*n + b):
			num += 1
			n += 1
		if num > maxnum:
			maxnum, maxa, maxb = (num, a, b)

print maxnum
print maxa
print maxb
print maxa*maxb
