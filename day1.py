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
        if x == cleanArray[-1]: #If x is the last item in the list, sum the group
            elfCalories.append(groupSum)
    else:
        elfCalories.append(groupSum)
        groupSum = 0

print (max(elfCalories))

### Part two ###

elfCalories.sort(reverse=True)
print(elfCalories[:3])
print(sum(elfCalories[:3]))
