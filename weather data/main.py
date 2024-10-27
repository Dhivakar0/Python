import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


gray_col = data["Primary Fur Color"] == "Gray"
grey_fur = data[gray_col]
red_fur = data[data["Primary Fur Color"] == "Cinnamon"]
black_fur = data[data["Primary Fur Color"] == "Black"]

grey_squirrils = len(grey_fur)
red_squirrils = len(red_fur)
black_squirrils = len(black_fur)

data_dict = {
    'color' : ["Gray", "Cinnamon", "Black"],
    'count' : [grey_squirrils, red_squirrils, black_squirrils]
}

squirrils = pandas.DataFrame(data_dict)

squirrils.to_csv("count1.csv")














