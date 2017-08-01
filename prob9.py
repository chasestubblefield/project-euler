import sys
for a in range(1, 1000):
	for b in range(1, 1000):
		for c in range(1, 1000):
			if a + b + c > 1000:
				break
			if a + b + c == 1000:
				if a*a + b*b == c*c:
					print a*b*c
					sys.exit()
