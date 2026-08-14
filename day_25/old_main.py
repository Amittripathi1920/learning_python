# # with open("day_25/weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)

# # import csv

# # with open("day_25/weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     print(data)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #         print(row)

# # print(temperatures)

# import pandas

# data = pandas.read_csv("day_25/weather_data.csv")

# temp_daily = data["temp"].to_list()

# total = 0
# count = len(temp_daily)

# for i in temp_daily:
#     total += i

# print(f"Total Sum of list is: {total} and AVG: {round((total/count),2)}")

# # to access fields
# print(round(data["temp"].mean(),2))
# # both works
# # print(data["condition"])
# # print(data.condition)

# # To access rows
# # print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# a = monday.temp * 9/5 + 32
# print(a)