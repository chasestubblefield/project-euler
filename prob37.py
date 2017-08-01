from euler_util import is_prime

def is_truncatable(n, leftToRight):
	if is_prime(n):
		if len(str(n)) == 1:
			return True
		if leftToRight:
			return is_truncatable(int(str(n)[1:]), True)
		else:
			return is_truncatable(int(str(n)[:-1]), False)
	else:
		return False

if __name__ == "__main__":
	p = 7
	s = 0
	n = 0
	target = 11
	while n < target:
		p += 1
		while not is_prime(p):
			p += 1
		if is_truncatable(p, True) and is_truncatable(p, False):
			s += p
			n += 1
	print s
