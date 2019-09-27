#1
#для целых и вещественных
def get_digit_sum(n):
    s = 0
    for i in str(abs(n)):
        if i == '.':
            continue
        else:
            s+= int(i)
    return s
