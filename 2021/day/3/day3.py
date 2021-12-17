def columnalGuideForOxygen(grid):
    columnalSum = []
    rows = len(grid)
    cols = len(grid[0])
    for i in range(cols):
        columnalSum.append(0)
    for row in grid:
        for i in range(cols):
            columnalSum[i] += row[i]
    columnalGuide = []
    for csum in columnalSum:
        if csum >= rows/2:
            columnalGuide.append(1)
        else:
            columnalGuide.append(0)
    return columnalGuide

def columnalGuideForCo2(grid):
    columnalSum = []
    rows = len(grid)
    cols = len(grid[0])
    for i in range(cols):
        columnalSum.append(0)
    for row in grid:
        for i in range(cols):
            columnalSum[i] += row[i]
    columnalGuide = []
    for csum in columnalSum:
        if csum < rows/2:
            columnalGuide.append(1)
        else:
            columnalGuide.append(0)
    return columnalGuide

class Diagnostic:
    def __init__(self, inputFile):
        self.grid = []
        self.columnalSum = []
        for line in inputFile:
            row = []
            for char in line.strip():
                row.append(int(char))
            self.grid.append(row)
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        for i in range(self.cols):
            self.columnalSum.append(0)
        for row in self.grid:
            for i in range(self.cols):
                self.columnalSum[i] += row[i]
        self.gamma = []
        self.epsilon = []
        for csum in self.columnalSum:
            if csum > self.rows/2:
                self.gamma.append(1)
                self.epsilon.append(0)
            else:
                self.gamma.append(0)
                self.epsilon.append(1)
        self.gammaRate = int("".join(map(str, self.gamma)), 2)
        self.epsilonRate = int("".join(map(str, self.epsilon)), 2)

        # Part 2
        self.oxygenFilter = self.grid.copy()
        self.co2Filter = self.grid.copy()

        oxygenIndex = 0
        while len(self.oxygenFilter) > 1:
            guide = columnalGuideForOxygen(self.oxygenFilter)
            filteredOxygen = filter(lambda line: line[oxygenIndex] == guide[oxygenIndex], self.oxygenFilter)
            self.oxygenFilter = list(filteredOxygen)
            oxygenIndex += 1

        co2Index = 0
        while len(self.co2Filter) > 1:
            guide = columnalGuideForCo2(self.co2Filter)
            filteredCo2 = filter(lambda line: line[co2Index] == guide[co2Index], self.co2Filter)
            self.co2Filter = list(filteredCo2)
            co2Index += 1

        self.finalOxygen = self.oxygenFilter[0]
        self.finalCo2 = self.co2Filter[0]

        self.oxygen = int("".join(map(str, self.finalOxygen)), 2)
        self.co2 = int("".join(map(str, self.finalCo2)), 2)

    def printReport(self):
        for row in self.grid:
            print(row)

    def printColumnalSum(self):
        print(self.columnalSum)

    def printSolution1(self):
        print('part1: ' + str(self.gammaRate * self.epsilonRate) + '\n')

    def printSolution2(self):
        for row in self.oxygenFilter:
                print(row)
        for row in self.co2Filter:
                print(row)

        print('part2: ' + str(self.oxygen * self.co2))


def part1():
    inputFile = open('/Users/laith/adventOfCode/2021/day/3/day3.txt')
    report = Diagnostic(inputFile)
    inputFile.close()
    report.printSolution1()

def part2():
    inputFile = open('/Users/laith/adventOfCode/2021/day/3/day3.txt')
    report = Diagnostic(inputFile)
    inputFile.close()
    report.printSolution2()


part1()
part2()
