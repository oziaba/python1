#2
a = input()
def get_digit_sum(n):
	return(sum(map(int,n)))
def is_beauty(n):
	return int(n) % get_digit_sum(n) == 0
print(is_beauty(a))
