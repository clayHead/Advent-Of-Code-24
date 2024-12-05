import math
from collections import Counter

class OrderRule:
    before = -1
    after = -1

    def __init__(self, input=None, left=None, right=None):
        if input == None and (left != None and right != None):
            self.before = left
            self.after = right
        else:
            split = input.strip().split("|")
            self.before = int(split[0])
            self.after = int(split[1])

    def __str__(self):
        return f'{self.before}|{self.after}'
    
    def __eq__(self, other):
        if self.before == other.before and self.after == other.after:
            return True
        return False
    
    def Contains(self, other):
        if self.before == other.before and self.after == other.after:
            return True
        elif self.after == other.before and self.before == other.after:
            return True
        return False
    
class Change:
    orderPages = []
    rules = list[OrderRule]

    def __init__(self, input):
        splits = input.strip().split(",")
        orderPageList = []
        for split in splits:
            orderPageList.append(int(split))
        self.orderPages = orderPageList

        rulesList = []
        for x in range(len(self.orderPages)-1):
            for y in range(x+1,len(self.orderPages)):
                rulesList.append(OrderRule(left=self.orderPages[x],right=self.orderPages[y]))
        self.rules = rulesList

    def __str__(self):
        return ','.join(str(x) for x in self.orderPages)
    
    def GetMiddle(self):
        return self.orderPages[math.floor(len(self.orderPages)/2)]
    
    def FixRules(self, rules, invalidRules):
        correctedRules = []
        # Go through all marked bad rules and find the correct rule using those 2 nums
        for badRule in invalidRules:
            for goodRule in rules:
                if goodRule.Contains(badRule):
                    correctedRules.append(goodRule)

        # Remove invalid rules and append corrected rules
        self.rules = [x for x in self.rules if x not in invalidRules]
        self.rules = self.rules + correctedRules

    def ReGenerateOrder(self):
        # Count occurances of first number in rule
        # Order of pages is determined by descending count of rules
        # GitHub CoPilot helped me to find the Count() class
        before_counts = Counter(rule.before for rule in self.rules)
        sortedList = sorted(before_counts, key=before_counts.get, reverse=True)

        # Last page in change does not have a rule where it appears first
        # Find the after in the rule that contains the rule that appears once
        # That after is the last page in the change
        for rule in self.rules:
            if rule.before == sortedList[-1]:
                sortedList += [rule.after]
        self.orderPages = sortedList

def Part1(changes, rules):
    sum = 0
    for change in changes:
        valid = True
        for rule in change.rules:
            if not rule in rules:
                valid = False
        if valid:
            sum += change.GetMiddle()

    print(sum)

def Part2(changes, rules):
    sum = 0
    for change in changes:
        valid = True
        invalidRules = []
        for rule in change.rules:
            if not rule in rules:
                valid = False
                invalidRules.append(rule)
        if not valid:
            change.FixRules(rules, invalidRules)
            change.ReGenerateOrder()
            sum += change.GetMiddle()
    print(sum)

with open('Day5\Day5.txt') as file:
    lines = file.readlines()

rules = []
changes = []

for line in lines:
    if '|' in line:
        rules.append(OrderRule(input=line))
    elif ',' in line:
        changes.append(Change(line))

Part1(changes, rules)

Part2(changes, rules)
