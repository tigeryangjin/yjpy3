while True:
    a = input('请输入第一个数字：')
    b = input('请输入第二个数字：')
    try:
        c = int(a) + int(b)
    except ValueError:
        print('输入的不是数字')
    else:
        print(c)
