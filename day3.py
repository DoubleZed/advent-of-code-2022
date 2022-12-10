import os
import string
### Part one ###
inputPath = os.path.join(os.getcwd(),"input","input_day3.txt")

array = [line.rstrip() for line in open(inputPath,"r")]

score = 0
for x in array:
    part1 = x[:len(x)//2]
    part2 = x[len(x)//2:]
 
    set_part1 = set(part1)
    set_part2 = set(part2)

    matched = set_part1 & set_part2

    score += string.ascii_letters.find(matched.pop())+1

print(score)

