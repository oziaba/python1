#4
def loop_file_generator():
    while True:
        text = open("./file1.txt", "r")
        for line in text:
            yield line
def len_file_generator():
    loop = loop_file_generator()
    x = map(len, loop)
    for i in x:
        yield i-1
len_str = len_file_generator()
for i in len_str:
    print(i)
