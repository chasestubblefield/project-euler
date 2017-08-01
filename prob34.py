from math import factorial

def is_curious(n):
	return sum([ factorial(int(digit)) for digit in str(n)]) == n

if __name__ == "__main__":
	print sum(filter(is_curious, range(145, 999999)))
