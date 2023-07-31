def count_words(file_name):
    # 计算一个文件大致包含多少个单词。
    try:
        with open(file_name, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f'Sorry, the file {file_name} does not exists.')
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f'The file {file_name} has about {num_words} words.')


def count_the_words(file_name):
    # 计算一个文件大致包含多少个单词。
    try:
        with open(file_name, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f'Sorry, the file {file_name} does not exists.')
        pass
    else:
        num_words = contents.lower().count('the ')
        print(f'The file {file_name} has about {num_words} words.')
    pass


filenames = ['d:\\Users\\tiger\\Documents\\Books\\IT\\Python编程从入门到实践（第二版）\\源代码文件\\chapter_10\\alice.txt',
             'd:\\Users\\tiger\\Documents\\Books\\IT\\Python编程从入门到实践（第二版）\\源代码文件\\chapter_10\\siddhartha.txt',
             'd:\\Users\\tiger\\Documents\\Books\\IT\\Python编程从入门到实践（第二版）\\源代码文件\\chapter_10\\moby_dick.txt',
             'd:\\Users\\tiger\\Documents\\Books\\IT\\Python编程从入门到实践（第二版）\\源代码文件\\chapter_10\\little_women.txt',
             'd:\\Users\\tiger\\Documents\\Books\\IT\\Python编程从入门到实践（第二版）\\源代码文件\\chapter_10\\tiger.txt']
for filename in filenames:
    count_the_words(filename)
