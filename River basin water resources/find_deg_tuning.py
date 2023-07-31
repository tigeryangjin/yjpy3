import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

file_path = 'd:\\Users\\tiger\\Documents\\Work\\YM\\project\\数字流域一期\\水位库容曲线拟合\\1449253200.csv'
df_original_data = pd.read_csv(file_path, sep=",|:|;", engine="python", header=0, encoding='gbk')
ndarray_curve_id = np.array(df_original_data.curve_id.to_list())
ndarray_water_lvl = np.array(df_original_data.water_lvl.to_list())
ndarray_lib_cap = np.array(df_original_data.lib_cap.to_list())
curve_id = ndarray_curve_id[0]
deg = 100
list_deg = []
list_sum_diff = []
# 拟合曲线
for i_deg in range(3, deg + 1):

    params = np.polyfit(ndarray_water_lvl, ndarray_lib_cap, i_deg)
    funcs = np.poly1d(params)

    # 最高水位
    # 最低水位
    min_water_lvl = np.min(ndarray_water_lvl)
    max_water_lvl = np.max(ndarray_water_lvl)

    # 存储水位库容数据
    list_polyfit_data = []
    # 最高水位与最低水位间循环
    i = min_water_lvl
    while i < max_water_lvl + 0.01:
        list_polyfit_data.append((curve_id, round(i, 2), round(funcs(i), 2)))
        i = i + 0.01

    df_polyfit_data = pd.DataFrame(list_polyfit_data, columns=['curve_id', 'water_lvl', 'polyfit_lib_cap'])

    df_original_data.curve_id = df_original_data.curve_id.astype('object')
    df_original_data.water_lvl = df_original_data.water_lvl.astype('object')
    df_polyfit_data.curve_id = df_polyfit_data.curve_id.astype('object')
    df_polyfit_data.water_lvl = df_polyfit_data.water_lvl.astype('object')

    df_merge_data = df_original_data.merge(df_polyfit_data, how='inner', on=['curve_id', 'water_lvl'])

    df_merge_data['diff'] = abs(df_merge_data.lib_cap - df_merge_data.polyfit_lib_cap)
    sum_diff = df_merge_data['diff'].sum()
    list_deg.append(i_deg)
    list_sum_diff.append(sum_diff)

min_sum_diff = min(list_sum_diff)
index = list_sum_diff.index(min_sum_diff)
min_deg = list_deg[index]
print('curve_id=', curve_id, ' ,min_deg=', min_deg, ' ,min_sum_diff', min_sum_diff)

plt.plot(list_deg, list_sum_diff, 'r', label='original values')
plt.legend()
# plt.show()
