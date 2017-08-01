from euler_util import is_palindrome

if __name__ == "__main__":
	count = 0
	for n in range(1, 10**4):
		m = n
		for i in range(53):
			m = m + int(str(m)[::-1])
			if is_palindrome(str(m)):
				count += 1
				if n == 47:
					print "OK"
				break
	print count



