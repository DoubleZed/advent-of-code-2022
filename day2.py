import os
import fnmatch
### Part one ###
inputPath = os.path.join(os.getcwd(),"input","input_day2.txt")

array = [line.rstrip() for line in open(inputPath,"r")]

def stringReplace(inputArray):
    newArray = [x.replace ('X', 'A') for x in inputArray]
    newArray2 = [x.replace ('Y', 'B') for x in newArray]
    newArray3 = [x.replace ('Z', 'C') for x in newArray2]
    return newArray3

def scoreBasedOnPick(input):
    answers = "ABC"
    return answers.rfind(input)+1

def scoreCountPart1(array):
    gamePoints = 0
    for x in array:
        gamePoints += scoreBasedOnPick(x[2])
        if x[0] == x[2]:
            gamePoints += 3
        else:
            if x[0] == "A":
                if x[2] == "B":
                    gamePoints += 6   
            elif x[0] == "B":
                if x[2] == "C":
                    gamePoints += 6
            elif x[0] == "C":
                if x[2] == "A":
                    gamePoints += 6          
    return gamePoints
            

print(scoreCountPart1(stringReplace(array)))
