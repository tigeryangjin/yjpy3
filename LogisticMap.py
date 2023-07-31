r_var = 2.6
x_var = 0.5
x_list = []


def lm(r, x):
    value = r * x * (1 - x)
    # value = 2 + x
    return value


for i in range(1, 20000):
    # print('i:', i, 'r_var:', r_var, 'x_var:', x_var)
    x_var = lm(r_var, x_var)
    x_list.append(x_var)

# print(x_list)

count_dict = {}
for key in x_list:
    count_dict[key] = count_dict.get(key, 0) + 1
    print(key, count_dict.get(key, 0))

for kv in count_dict.items():
    if kv[1] > 200:
        print(r_var, kv[0])

print(count_dict)
# print(count_dict.get(0.8421543994326705,0))

# print(x_list)
