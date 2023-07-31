def k_con(n):
    list_n = []
    dict_n = {'key:': n}
    while n > 1:
        if (n % 2) == 0:
            n = n / 2
            list_n.append(int(n))
        else:
            n = n * 3 + 1
            list_n.append(int(n))
    dict_n['seq'] = list_n
    print(dict_n)


# k_con(1)
# k_con(2)
k_con(476)
k_con(27)
# k_con(4)
# k_con(5)
# k_con(6)
# k_con(7)
# k_con(8)
# k_con(9)
# k_con(10)
# k_con(11)
# k_con(999)
