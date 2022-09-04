# def part1():
#     inputFile = open('/Users/laith/adventOfCode/2021/day3/test.txt')
#     for line in inputFile:
#         pass
#     print('part 1: ' + str(1))

# def part2():
#     inputFile = open('/Users/laith/adventOfCode/2021/day3/test.txt')
#     for line in inputFile:
#         pass
#     print('part 2: ' + str(2))

# part1()
# part2()


def part1():
    inputFile = open('/Users/laith/adventOfCode/2021/day/1/input.txt')
    increasing = 0
    prevNum = float('inf')
    for line in inputFile:
        currNum = int(line)
        if currNum > prevNum:
            increasing += 1
        prevNum = currNum
    print("part 1: " + str(increasing))
    inputFile.close()

def part2():
    inputFile = open('/Users/laith/adventOfCode/2021/day/1/input.txt')
    listNums = []
    for line in inputFile:
        listNums.append(int(line))

    increasing = 1
    prevSum = float('inf')
    for i in range(len(listNums) - 3):
        currSum = listNums[i] + listNums[i + 1] + listNums[i + 2]
        if currSum > prevSum:
            increasing += 1
        prevSum = currSum
    print('part 2: ' + str(increasing))
    inputFile.close()

part1()
part2()
