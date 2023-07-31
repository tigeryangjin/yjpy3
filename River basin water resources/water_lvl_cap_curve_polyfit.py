import csv
import numpy as np

import matplotlib.pyplot as plt

# 从csv中读取水位库容数据
water_lvl_list = []
lib_cap_list = []
# 读取csv文件
with open('d:\\Users\\tiger\\Documents\\Work\\YM\\project\\数字流域一期\\水位库容曲线拟合\\1449253200.csv', "r", encoding='utf8',
          newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        water_lvl_list.append(row[1])
        lib_cap_list.append(row[2])

water_lvl_list.remove('water_lvl')
lib_cap_list.remove('lib_cap')
water_lvl = np.array(list(map(float, water_lvl_list)))
lib_cap = np.array(list(map(float, lib_cap_list)))
# data_pid:
# water_lvl:水位值
# lib_cap:库容值
data_pid = '1449253200'
deg = 3
# water_lvl = np.array([80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93])
# lib_cap = np.array([4.3, 6.4, 9.1, 12.5, 16.5, 20.8, 25.5, 30.6, 36, 41.5, 47.3, 53.5, 60, 66.8])

# 拟合曲线
params = np.polyfit(water_lvl, lib_cap, deg)
funcs = np.poly1d(params)
# print(funcs)
# print(funcs(88))

# 最高水位
# 最低水位
min_water_lvl = np.min(water_lvl)
max_water_lvl = np.max(water_lvl)

# 存储水位库容数据
list_data = []
# 最高水位与最低水位间循环
i = min_water_lvl
while i < max_water_lvl + 0.01:
    list_data.append((data_pid, round(i, 2), round(funcs(i), 2)))
    i = i + 0.01

# print(list_data)

# 写入csv
title = ['data_pid', 'water_lvl', 'lib_cap']
with open('d:\\Users\\tiger\\Documents\\Work\\YM\\project\\数字流域一期\\水位库容曲线拟合\\111025000_polyfit.csv', 'w',
          encoding='utf-8', newline='') as file_obj:
    # 1:创建writer对象
    writer = csv.writer(file_obj)
    # 2:写表头
    writer.writerow(title)
    # 3:遍历列表，将每一行的数据写入csv
    for j in list_data:
        writer.writerow(j)

# 曲线画图
y_lib_cap = funcs(water_lvl)  # 拟合y值
plt.plot(water_lvl, lib_cap, 's', label='original values')
plt.plot(water_lvl, y_lib_cap, 'r', label='Power series')
plt.legend()
plt.show()
