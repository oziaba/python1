#5
def loop_file_generator():
    while True:
        text = open("./file1.txt", "r")
        for line in text:
            yield line
def nod19_in_file_generator():
    loop = list(loop_file_generator())
    filt = list(filter(lambda x: 'NOD19' in x, loop))
    yield filt
res = nod19_in_file_generator()
for i in res:
    print(i)
