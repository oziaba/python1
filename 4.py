#4
a = input()
def is_prime(n):
	n = int(n)
	d = 2
	while n % d != 0:
		d += 1
	return d == n
print(is_prime(a))
