import os
import fnmatch
### Part one ###
inputPath = os.path.join(os.getcwd(),"input","input_day2.txt")

array = [line.rstrip() for line in open(inputPath,"r")]

gamePoints = 0
for x in array:
    if fnmatch.fnmatch(x, 'A*'):
        if fnmatch.fnmatch(x, '*X'):
            gamePoints += 3
            gamePoints += 1
        elif fnmatch.fnmatch(x, '*Y'):
            gamePoints += 6
            gamePoints += 2
        elif fnmatch.fnmatch(x, '*Z'):
            gamePoints += 0
            gamePoints += 3
    elif fnmatch.fnmatch(x, 'B*'):
        if fnmatch.fnmatch(x, '*X'):
            gamePoints += 0
            gamePoints += 1
        elif fnmatch.fnmatch(x, '*Y'):
            gamePoints += 3
            gamePoints += 2
        elif fnmatch.fnmatch(x, '*Z'):
            gamePoints += 6
            gamePoints += 3
    elif fnmatch.fnmatch(x, 'C*'):
        if fnmatch.fnmatch(x, '*X'):
            gamePoints += 6
            gamePoints += 1
        elif fnmatch.fnmatch(x, '*Y'):
            gamePoints += 0
            gamePoints += 2
        elif fnmatch.fnmatch(x, '*Z'):
            gamePoints += 3
            gamePoints += 3
 
print ("Total points:", gamePoints)
