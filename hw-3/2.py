#2
def devider_generator(number):
    for i in range(1, int(number/2)+1):
        if number % i == 0:
            yield i
    yield number
deviders = devider_generator(1024)
for i in deviders:
    print(i)
