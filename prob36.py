def is_palindrome(s):
	length = len(s)
	if length == 1:
		return True
	if s[0] == s[length-1]:
		if length == 2:
			return True
		else:
			return is_palindrome(s[1:length-1])
	else:
		return False

def binary_rep(x):
    return ''.join(str((x>>i)&1) for i in xrange(32-1,-1,-1)).lstrip('0')

if __name__ == "__main__":
	sum = 0
	for n in range(1, 1000000):
		if is_palindrome(str(n)) and is_palindrome(binary_rep(n)):
			sum += n
	print sum
