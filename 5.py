#5
a = input()
def is_self_dividing(n):
	for i in n:
		if int(n) % int(i) == 0:
			return True
        else:
            return False
print(is_self_dividing(a))
