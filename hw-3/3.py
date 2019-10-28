#3
def loop_file_generator():
    while True:
        text = open("./file1.txt", "r")
        for line in text:
            yield line
loop = loop_file_generator()
for i in loop:
    print(i)
