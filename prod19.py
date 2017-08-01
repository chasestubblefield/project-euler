def is_leap(year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return True
			else:
				return False
		return True
	return False

def days_in_month(month, year):
	if month == 2:
		if is_leap(year):
			return 29
		else:
			return 28
	if month in  [4, 6, 9, 11]:
		return 30
	else:
		return 31

if __name__ == "__main__":
	year_in_days = 30 * 4 + 28 + 31*7
	leap_year_in_days = year_in_days + 1
	day = (1 + leap_year_in_days) % 7
	count = 0
	for year in range(1901, 2001):
		for month in range(1, 13):
			if day == 0:
				count += 1
			day = (day + days_in_month(month, year)) % 7
	print count
