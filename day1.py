import os
import pandas as pd
### Part one ###
inputPath = os.path.join(os.getcwd(),"input","input_day1.txt")

array = [line.rstrip() for line in open(inputPath,"r")]

cleanArray = []
for x in array:
    if x != "":
        cleanArray.append(int(x))
    else:
        cleanArray.append(x) 

elfCalories = []
groupSum = 0
for x in cleanArray:
    if isinstance(x, int):
        groupSum = groupSum + x
    else:
        elfCalories.append(groupSum)
        groupSum = 0

print (max(elfCalories))
