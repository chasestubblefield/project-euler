largest = 0
largest_start = 0
for starting in range(1, 1000000):
	length = 1
	current = starting
	while current > 1:
		if current % 2 == 0:
			current = current / 2
		else:
			current = 3 * current + 1
		length += 1
	if length > largest:
		largest = length
		largest_start = starting
print largest_start
