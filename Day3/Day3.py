import re
patern = "mul\((\d{1,3},\d{1,3})\)"

def Part1(lines):
    sum = 0

    for line in lines:
        matches = re.findall(patern, line)

        for match in matches:
            split = match.split(',')

            var1 = int(split[0])
            var2 = int(split[1])

            sum += var1 * var2
    
    return sum

def Part2(lines):
    sum = 0
    instructions = []
    mulEnabled = True

    for line in lines:
        # Parse the lines charecter by charecter
        for x in range(len(line)):
            # First check if we need to enable/disable mul
            if (line[x] == 'd'):
                if (line[x:x+4] == 'do()'):
                    #print('enabled')
                    mulEnabled = True
                elif (line[x:x+7] == 'don\'t()'):
                    #print('disabled')
                    mulEnabled = False
            elif (line[x] == 'm' and mulEnabled):
                if (line[x:x+4] == 'mul('):
                    # Start after where we know the numerics are and work until the biggest possbile instruction
                    # Find the end paren and then create an instriction based off that
                    add = 5
                    for i in range(add,13):
                        print(line[x:x+add])
                        if (line[x+add] == ')'):
                            instructions.append(line[x:x+add])
                            break
                        else:
                            add += 1
    
    for instruction in instructions:
        # The above parsing includes results like mul(75), exclude these
        if ',' in instruction:
            # Strip away all chars before and after ints and ','
            instruction = instruction.replace('mul(', '')
            instruction = instruction.replace(')', '')

            print(instruction)
            split = instruction.split(',')
            var1 = int(split[0])
            var2 = int(split[1])
            
            sum += var1 * var2

    return sum

with open('Day3\Day3.txt') as file:
    lines = file.readlines()

sum1 = Part1(lines)
sum2 = Part2(lines)

print("Part1: " + str(sum1) + ", Part2: " + str(sum2))