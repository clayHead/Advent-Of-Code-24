class Grid:
    lines = []
    yBound = -1
    xBound = -1
    xCrossBound = -1
    yCrossBound = -1

    def __init__(self, lines):
        self.lines = lines
        self.xBound = len(self.lines)-3
        self.yBound = len(self.lines[0])-4
        self.xCrossBound = len(self.lines)-1
        self.yCrossBound = len(self.lines[0])-2

    def __str__(self):
        string = ''
        for line in self.lines:
            for i in range(len(line)):
                string += line[i]
            string += '\n'
        return string
    
    def At(self, x, y):
        return self.lines[x][y]

    def CheckUp(self, x, y):
        if x > 2:
            if self.At(x,y) + self.At(x-1,y) + self.At(x-2,y) + self.At(x-3,y) == 'XMAS':
                return True
        else: 
            return False
    
    def CheckDown(self, x, y):
        if x < self.xBound:
            if self.At(x,y) + self.At(x+1,y) + self.At(x+2,y) + self.At(x+3,y) == 'XMAS':
                return True
        else:
            return False
    
    def CheckLeft(self, x, y):
        if y > 2:
            if self.At(x,y) + self.At(x,y-1) + self.At(x,y-2) + self.At(x,y-3) == 'XMAS':
                return True
        else: 
            return False
        
    def CheckRight(self, x, y):
        if y < self.yBound:
            if self.At(x,y) + self.At(x,y+1) + self.At(x,y+2) + self.At(x,y+3) == 'XMAS':
                return True
        else:
            return False
    
    def CheckUpRight(self, x, y):
        if y < self.yBound and x > 2:
            if self.At(x,y) + self.At(x-1,y+1) + self.At(x-2,y+2) + self.At(x-3,y+3) == 'XMAS':
                return True
        else:
            return False
        
    def CheckUpLeft(self, x, y):
        if y > 2 and x > 2:
            if self.At(x,y) + self.At(x-1,y-1) + self.At(x-2,y-2) + self.At(x-3,y-3) == 'XMAS':
                return True
        else:
            return False
        
    def CheckDownRight(self, x, y):
        if x < self.xBound and y < self.yBound:
            if self.At(x,y) + self.At(x+1,y+1) + self.At(x+2,y+2) + self.At(x+3,y+3) == 'XMAS':
                return True
        else:
            return False
    
    def CheckDownLeft(self, x, y):
        if x < self.xBound and y > 2:
            if self.At(x,y) + self.At(x+1,y-1) + self.At(x+2,y-2) + self.At(x+3,y-3) == 'XMAS':
                return True
        else:
            return False
    
    def CheckAll(self, x, y):
        count = 0
        if (self.CheckUp(x,y)):
            count += 1
        if (self.CheckDown(x,y)):
            count += 1
        if (self.CheckLeft(x,y)):
            count += 1
        if (self.CheckRight(x,y)):
            count += 1
        if (self.CheckUpRight(x,y)):
            count += 1
        if (self.CheckUpLeft(x,y)):
            count += 1
        if (self.CheckDownRight(x,y)):
            count += 1
        if (self.CheckDownLeft(x,y)):
            count += 1
        return count
    
    def ScanList(self):
        countPart1 = 0
        countPart2 = 0

        for x in range(len(self.lines)):
            for y in range(len(self.lines[0])-1):
                countPart1 += self.CheckAll(x, y)
                if self.CheckX(x,y):
                    countPart2 += 1
        
        print('Part1: ' + str(countPart1) + ", Part2: " + str(countPart2))

    def CheckX(self, x, y):
        if x > 0 and x < self.xCrossBound and y > 0 and y < self.yCrossBound:
            if self.At(x,y) == 'A':
                topLeft = self.At(x-1,y-1)
                topRight = self.At(x-1,y+1)
                bottomLeft = self.At(x+1,y-1)
                bottomRight = self.At(x+1,y+1)
                if (((topLeft == 'M' and bottomRight == 'S') or (topLeft == 'S' and bottomRight == 'M')) and
                   ((topRight == 'M' and bottomLeft == 'S') or (topRight == 'S' and bottomLeft == 'M'))):
                    return True
                

with open('Advent-Of-Code-24\Day4\Day4.txt') as file:
    lines = file.readlines()

grid = Grid(lines)

grid.ScanList()