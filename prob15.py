import math

def choose(n, r):
	f = math.factorial
	return f(n) / f(r) / f(n-r)

if __name__ == "__main__":
	n = 20
	print choose(2 * n, n)
