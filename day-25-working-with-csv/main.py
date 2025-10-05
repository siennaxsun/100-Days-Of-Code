
"""
import csv

with open ("weather_data.csv") as weather_file:
    data = csv.reader(weather_file)

    temperatures = []
    for row in data:
        print(row)
        item_2 = row[1]
        if item_2 != "temp":
            temperatures.append(int(item_2))

    print(temperatures)
"""


"""
# import pandas library
import pandas

# use the library by using pandas.xxx
data = pandas.read_csv("weather_data.csv")
print (type(data))
print(type(data["temp"]))

# convert the dataframe object to dictionary
data_dict = data.to_dict()
print(data_dict)

# convert the series into a list
temp_list = data["temp"].to_list()
print(temp_list)

# using sum() built in function in python
avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)

# using for loop
sum_temp = 0
for temp in temp_list:
    sum_temp += temp
avg_tem = sum_temp / len(temp_list)
print(avg_temp)

# using pandas library
avg_temp = data["temp"].mean()
print(avg_temp)

condition = data["condition"]
print(condition)

# because pandas converts the heading of each column into attribute, so you can
# also just use the dot notation to get the series list
print(data.condition)


# get data in row
print(data[data.day == "Monday"])

# get the row with the highest temperature
max_temp = data["temp"].max()
print (max_temp)
print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
mon_condition = monday.condition[0]
print(mon_condition)

mon_temp = monday.temp[0]
print(mon_temp)



# create a dataframe from scratch from a dictionary
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "Scores": [76, 56, 65]
}
# initilize the Pandas Dataframe class with our data
data = pandas.DataFrame(data_dict)
print(data)

# convert the dataframe to csv file
data_csv = data.to_csv("new_data.csv")
print(data_csv)

"""


# squirrel project
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240321.csv")
# print(data)

grey_squirrel = data[data["Primary Fur Color"] == "Gray"]
grey_count = len(grey_squirrel)
print (grey_count)

cinnamon_squirrel = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_count = len(cinnamon_squirrel)

black_squirrel = data[data["Primary Fur Color"] == "Black"]
black_count = len(black_squirrel)

fur_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_count, cinnamon_count, black_count]
}

fur_color_dataframe = pandas.DataFrame(fur_dict)
print(fur_color_dataframe)


fur_color_csv = fur_color_dataframe.to_csv("squirrel_count.csv")

