num = 1
for n in range(2, 100):
	num *= n
num = str(num)
sum = 0
for digit in num:
	sum += int(digit)
print sum
