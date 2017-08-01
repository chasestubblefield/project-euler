from itertools import permutations
from euler_util import is_prime

def rotate(n):
	num = str(n)
	if len(num) > 1:
		num = "".join([num[-1], num[:-1]])
	return int(num)


def is_circular(n):
	if is_prime(n):
		r = rotate(n)
		while (r != n):
			if not is_prime(r):
				return False
			r = rotate(r)
		return True
	else:
		return False

if __name__ == "__main__":
	print len(filter(is_circular, range(2, 1000000)))
