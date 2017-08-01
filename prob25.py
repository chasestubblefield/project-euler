prev = 1
term = 1
num = 2
while len(str(term)) < 1000:
	new = prev + term
	prev = term
	term = new
	num += 1
print num
