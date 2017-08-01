def digit_counts(n):
	counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for digit in str(n):
		counts[int(digit)] += 1
	return counts

if __name__ == "__main__":
	x = 1
	target = 6
	while True:
		counts = digit_counts(x)
		good = True
		for c in range(2, target+1):
			if counts != digit_counts(c*x):
				good = False
				break
		if good:
			break
		else:
			x += 1
	print x
