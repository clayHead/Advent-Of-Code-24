with open('/Users/claytonjohnson/Documents/Advent-Of-Code/AoC24/Advent-Of-Code-24/Day1/Day1.txt') as file:
    lines = file.readlines()

list1 = []
list2 = []

for line in lines:
    split = line.split()

    list1.append(int(split[0]))
    list2.append(int(split[1]))

list1.sort()
list2.sort()

distance = 0

for x in range(len(list1)):
    distance += abs(list1[x] - list2[x])

print(distance)