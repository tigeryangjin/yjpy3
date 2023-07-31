import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.style.use('tableau-colorblind10')
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
plt.show()
