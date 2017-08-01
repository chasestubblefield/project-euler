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

list = range(100,1000)
prods = [n*m for n in list for m in list]
prods.sort()
prods.reverse()
largest = None
for p in prods:
	if is_palindrome(str(p)):
		largest = p
		break
print largest
