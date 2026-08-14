import pandas as pd

data = pd.read_csv("day_25/squirrels.csv")
# df = pd.DataFrame(data)
# print(df.head())

# color = df["Primary Fur Color"].unique()

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray" ,"Red" ,    "Black" ],
    "Count" : [gray_count, Cinnamon_count, Black_count]
}

data_op = pd.DataFrame(data_dict)
data_op.to_csv("day_25/Squirrels_Count.csv")

