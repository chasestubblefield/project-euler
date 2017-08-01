sum = 2
prev = 2
term = 3
while term < 4000000:
	if term % 2 == 0:
		sum += term
	new = term + prev
	prev = term
	term = new
print sum
