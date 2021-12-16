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

    def printReport(self):
        for row in self.grid:
            print(row)

    def printColumnalSum(self):
        for i in range(self.cols):
            self.columnalSum.append(0)
        for row in self.grid:
            for i in range(self.cols):
                self.columnalSum[i] += row[i]
        print("columnalSum:")
        print(self.columnalSum)
        print('rows:')
        print(self.rows)

def part1():
    inputFile = open('/Users/laith/adventOfCode/2021/day/3/test.txt')
    report = Diagnostic(inputFile)
    print('part 1:')
    report.printReport()
    report.printColumnalSum()

def part2():
    inputFile = open('/Users/laith/adventOfCode/2021/day/3/test.txt')
    for line in inputFile:
        pass
    print('\npart 2: ' + str(2))



part1()
part2()
