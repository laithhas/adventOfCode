# Problem: https://adventofcode.com/2021/day/2

def part1():
    inputFile = open('/Users/laith/adventOfCode/2021/day2/day2.txt')
    depth = 0
    horizontal = 0
    for line in inputFile:
        movement, distance = line.split()
        distanceValue = int(distance)
        if movement == 'forward':
            horizontal += distanceValue
        elif movement == 'down':
            depth += distanceValue
        elif movement == 'up':
            depth -= distanceValue
    print('part 1: ' + str(depth * horizontal))

def part2():
    inputFile = open('/Users/laith/adventOfCode/2021/day2/day2.txt')
    depth = 0
    horizontal = 0
    aim = 0
    for line in inputFile:
        movement, distance = line.split()
        distanceValue = int(distance)
        if movement == 'forward':
            horizontal += distanceValue
            depth += aim * distanceValue
        elif movement == 'down':
            aim += distanceValue
        elif movement == 'up':
            aim -= distanceValue
    print('part 2: ' + str(depth * horizontal))

part1()
part2()
