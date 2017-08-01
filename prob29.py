if __name__ == "__main__":
	terms = set()
	n = 100
	for a in range(2, n+1):
		for b in range(2, n+1):
			terms.add(a**b)
	print len(terms)
