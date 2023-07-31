import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.style.use('tableau-colorblind10')
x_values = range(1, 5001)
y_values = [x ** 3 for x in x_values]
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)
ax.axis([0, 5100, 0, 125100000000])
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
plt.show()
