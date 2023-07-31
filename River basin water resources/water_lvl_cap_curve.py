import csv
import numpy as np
import matplotlib.pyplot as plt
from numpy import polynomial as poly

# data_pid:
# water_lvl:水位值
# lib_cap:库容值
data_pid = '1065215000'
water_lvl = np.array([318,338,340.5,348])
lib_cap = np.array([0,20,30.003,50])

# 使用 Power series 拟合
pf = poly.polynomial.Polynomial.fit(water_lvl, lib_cap, deg=10)

# 使用 Chebyshev series 拟合
# c = poly.chebyshev.Chebyshev.fit(water_lvl, lib_cap, deg=2)

# 表达式
# print(p)
# 27.888616071428533 + 32.79496793035394·x¹ - 7.495312500000063·x² + 1.5509553253119517·x³
# print(p(80))

# 最高水位
# 最低水位
min_water_lvl = np.min(water_lvl)
max_water_lvl = np.max(water_lvl)

list_data = []

i = min_water_lvl
while i < max_water_lvl + 0.01:
    # print(round(i, 2), round(p(i), 2))
    list_data.append((data_pid,round(i, 2), round(pf(i), 2)))
    i = i + 0.01

# print(list_data)

# 写入csv
title = ['data_pid', 'water_lvl', 'lib_cap']
with open('water_lvl_cap_curve.csv', 'w', encoding='utf-8', newline='') as file_obj:
    # 1:创建writer对象
    writer = csv.writer(file_obj)
    # 2:写表头
    writer.writerow(title)
    # 3:遍历列表，将每一行的数据写入csv
    for j in list_data:
        writer.writerow(j)

p_curve = p(water_lvl)  # 拟合y值
c_curve = c(water_lvl)

plt.plot(water_lvl, lib_cap, 's', label='original values')
plt.plot(water_lvl, p_curve, 'r', label='Power series')
plt.plot(water_lvl, c_curve, 'g--', label='Chebyshev series')
plt.legend()
plt.show()
