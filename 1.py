#1
def get_digit_sum(n):
	s = 0
	while n != 0:
		s += n % 10
		n = n // 10
	return s
