file = open("names.txt")
names = sorted([ s[1:len(s)-1] for s in file.readline().split(",") ])
sum = 0
for i, name in enumerate(names):
	value = 0
	for letter in name:
		value += ord(letter) - ord('A') + 1
	place = i + 1
	sum += value * place
print sum
