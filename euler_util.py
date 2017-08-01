import math

def sum_digits(n):
  return sum([int(digit) for digit in str(n)])

def sum_letters(w):
  return sum([ ord(letter) - ord('A') + 1 for letter in w ])

def is_prime(n):
  if n < 2:
    return False
  for m in range(2, int(math.sqrt(n)) + 1):
    if n % m == 0:
      return False
  return True

def is_triangle(n):
  term = 1
  i = 1
  while (term < n):
    i += 1
    term = int(i * (i + 1) / 2)
  return term == n


def divisors(n):
  list = []
  for i in range(1, int(math.sqrt(n) + 1)):
    if n % i == 0:
      list.append(i)
      list.append(int(n / i))
  if math.sqrt(n) == int(math.sqrt(n)):
    list.append(int(math.sqrt(n)))
  return sorted(list)

def proper_divisors(n):
  return divisors(n)[:-1]

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
