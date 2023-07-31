import pandas as pd

import numpy as np

# url = "https://raw.github.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/tips.csv"
url = "d:/Users/tiger/Documents/tips.csv"
tips = pd.read_csv(url)

# print(tips[(tips["time"] == 'Dinner') & (tips["tip"] > 5)])
# print(tips[(tips["time"] == 'Lunch') & (tips["tip"] > 5)])

frame = pd.DataFrame(
    {"col1": ["A", "B", np.NaN, "C", "D"],
     "col2": ["F", np.NaN, "G", "H", "I"]}
)
# print(frame)
# print(frame[frame["col2"].isna()])
# print(tips.groupby("sex").size())
# print(tips.groupby("sex").count())
# print(tips.groupby("day").agg({"tip": np.mean, "day": np.size}))

df1 = pd.DataFrame({"key": ["A", "B", "C", "D"], "value": np.random.randn(4)})
df2 = pd.DataFrame({"key": ["B", "D", "D", "E"], "value": np.random.randn(4)})

print(df1)
print(df2)
