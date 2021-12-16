def part1():
    inputFile = open('/Users/laith/adventOfCode/2021/day3/test.txt')
    grid = []
    for line in inputFile:
        row = []
        for char in line.strip():
            row.append(int(char))
        print(row)

    print('part 1: ' + str(1))

def part2():
    inputFile = open('/Users/laith/adventOfCode/2021/day3/test.txt')
    for line in inputFile:
        pass
    print('part 2: ' + str(2))

def columnalSum(grid):
    for row in grid:
        for value in row:
            pass



part1()
part2()
