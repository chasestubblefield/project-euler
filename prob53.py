import math

def choose(n, r):
	f = math.factorial
	return f(n) / f(r) / f(n-r)

if __name__ == "__main__":
	print len([True for n in range(1, 101) for r in range(1, n) if choose(n, r) > 10**6])

