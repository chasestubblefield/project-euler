from euler_util import sum_letters

def is_triangle(n):
	term = 1
	i = 1
	while (term < n):
		i += 1
		term = int(i * (i + 1) / 2)
	return term == n

if __name__ == "__main__":
	print len(filter(is_triangle, [sum_letters(s[1:-1]) for s in open("words.txt").readline().split(",")]))
