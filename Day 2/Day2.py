def check_report(report):
    first = report[0]
    second = report[1]
    if (first > second):
        increasing = False
    elif (first < second):
        increasing = True
    else:
        return 0

    safe = True
    for i in range(1, len(report)):
        if (increasing and report[i] < report[i-1]):
            safe = False
            break
        elif (not increasing and report[i] > report[i-1]):
            safe = False
            break
        if (abs(report[i] - report[i-1])) > 3 or (abs(report[i] - report[i-1])) < 1:
            safe = False
            break
    
    if (safe is True):
        return 1
    return 0

with open('/Users/claytonjohnson/Documents/Advent-Of-Code/AoC24/Advent-Of-Code-24/Day 2/Day2.txt') as file:
    lines = file.readlines()

reports = []

for line in lines:
    split = line.split()

    levels = []
    for var in split:
        levels.append(int(var))

    reports.append(levels)

safeCount = 0
dampenerOn = True

for report in reports:
    safe = check_report(report)

    if (safe == 1):
        safeCount+=1
    elif (safe == 0 and dampenerOn):
        for i in range(len(report)):
            dampened = report[:]
            dampened.pop(i)
            safe = check_report(dampened)
            if (safe == 1):
                safeCount+=1
                break
        
print(safeCount)