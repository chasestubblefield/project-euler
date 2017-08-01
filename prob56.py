from euler_util import sum_digits

if __name__ == "__main__":
	max = 1
	for a in range(100):
		for b in range(100):
			s = sum_digits(a**b)
			if s > max:
				max = s
	print max
