from euler_util import *
import itertools

def is_abundant(n):
	return sum(proper_divisors(n)) > n

if __name__ == "__main__":
	abundant_nums = filter(is_abundant, range(12, 28123+1))
	can_be_written = set()
	for a, b in itertools.product(abundant_nums, abundant_nums):
		can_be_written.add(a+b)
	print sum(filter(lambda x: not x in can_be_written, range(24, 28123+1)))

