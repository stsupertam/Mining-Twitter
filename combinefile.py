# -*- coding: utf-8 -*-

import os
import codecs

data = []
data.append('date;attention;id;permalink;tag;text\n')
for fn in os.listdir('./dataset'):
    if fn != 'Readme.txt' and fn != 'outputdata.csv':
        filename = "./dataset/" + fn 
        with codecs.open(filename, 'r', 'utf-8') as file:
            for row in file:
                if row != 'date;attention;id;permalink;tag;text\n':
                    data.append(row)

with codecs.open('./dataset/outputdata.csv', 'w', 'utf-8') as file:
    for row in data:
        file.write(row)
    

