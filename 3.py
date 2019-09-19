#3
a = input()
def is_power_of_two(n):
	n = int(n)
	while n > 1:
		n /= 2
	if n == 1:
		print('True')
	else:
		print('False')
