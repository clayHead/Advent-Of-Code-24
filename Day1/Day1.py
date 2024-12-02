def GetDistance(list1, list2):
    distance = 0

    for x in range(len(list1)):
        distance += abs(list1[x] - list2[x])

    return distance

def GetSimilarity(list1, list2):
    similarity = 0

    for left in list1:
        numRepeats = 0

        for right in list2:
            if left == right:
                numRepeats += 1
        
        similarity += left * numRepeats

    return similarity

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

distance = GetDistance(list1, list2)
similarity = GetSimilarity(list1, list2)

print(distance, similarity)