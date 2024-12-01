with open('/Users/claytonjohnson/Documents/Advent-Of-Code/AoC24/Advent-Of-Code-24/Day1/Day1.txt') as file:
    lines = file.readlines()

list1 = []
list2 = []

for line in lines:
    split = line.split()

    list1.append(int(split[0]))
    list2.append(int(split[1]))

similarity = 0

for left in list1:
    numRepeats = 0

    for right in list2:
        if left == right:
            numRepeats += 1
    
    similarity += left * numRepeats

print(similarity)