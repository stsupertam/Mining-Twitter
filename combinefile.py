import os

data = []
count = 0
data.append("date;attention;id;permalink;tag;text")
for fn in os.listdir('./dataset'):
    if fn != 'Readme.txt':
        filename = "./dataset/" + fn 
        with open(filename, 'r') as file:
            for row in file:
                count += 1
                if row != "date;attention;id;permalink;tag;text":
                    data.append(row)

with open("./dataset/outputdata.csv", 'w') as file:
    for row in data:
        file.write(row)
    

