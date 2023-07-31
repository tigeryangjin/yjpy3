filename = 'd:\\Users\\tiger\\Documents\\Books\\IT\\Python编程从入门到实践（第二版）\\源代码文件\\chapter_10\\alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f'Sorry, the file {filename} does not exists.')
else:
    words = contents.split()
    num_words = len(words)
    print(f'The file {filename} has about {num_words} words.')
