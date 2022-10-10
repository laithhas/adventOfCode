# Problem: https://adventofcode.com/2021/day/5
'''day 5'''

# def part1():
#     '''part1'''
#     input_file = open('/Users/laith/adventOfCode/2021/day/5/test.txt', encoding="utf-8")
#     input_file.close()


# def part2():
#     '''part2'''
#     input_file = open('/Users/laith/adventOfCode/2021/day/5/test.txt', encoding="utf-8")
#     input_file.close()

# part1()
# part2()

class Vent:
    ''' A class representing a hydrothermal vent from the problem in day 5 '''
    def __init__(self, input_file_path) -> None:
        input_file = open(input_file_path, encoding="utf-8")
        max_x, max_y = 0, 0
        self.lines = []
        for line in input_file:
            left_coord, right_coord = line.split(' -> ')
            x1, y1 = [int(s) for s in left_coord.strip().split(',')]
            x2, y2 = [int(s) for s in right_coord.strip().split(',')]
            self.lines.append(((x1, y1), (x2, y2)))
            max_x = max(max_x, x1, x2)
            max_y = max(max_y, y1, y2)
        self.grid = [[0] * (max_x + 1) for i in range(max_y + 1)]
        input_file.close()


    def apply_straight_lines_to_grid(self) -> None:
        ''' Take straight lines from self.lines and update grid accordingly '''
        for line in self.lines:
            x1, y1 = line[0][0], line[0][1]
            x2, y2 = line[1][0], line[1][1]

            if x1 == x2 and y1 == y2:
                print('same point')
            elif x1 == x2:
                lesser_y = min(y1, y2)
                greater_y = max(y1, y2)
                for i in range(lesser_y, greater_y + 1):
                    self.grid[i][x1] += 1
            elif y1 == y2:
                lesser_x = min(x1, x2)
                greater_x = max(x1, x2)
                for i in range(lesser_x, greater_x + 1):
                    self.grid[y1][i] += 1
            else:
                pass # diagonal line

    def apply_diagonal_lines_to_grid(self) -> None:
        ''' Take diagonal lines from self.lines and update grid accordingly '''
        for line in self.lines:
            x1, y1 = line[0][0], line[0][1]
            x2, y2 = line[1][0], line[1][1]

            if x1 == x2 and y1 == y2:
                print('same point')
            elif x1 == x2:
                pass # vertical line
            elif y1 == y2:
                pass # horizontal line
            elif x1 < x2 and y1 < y2: # SE diagonal
                diff = x2 - x1
                for i in range(diff + 1):
                    self.grid[y1 + i][x1 + i] += 1
            elif x1 > x2 and y1 > y2: # NW diagonal
                diff = x1 - x2
                for i in range(diff + 1):
                    self.grid[y1 - i][x1 - i] += 1
            elif x1 < x2 and y1 > y2: # NE diagonal
                diff = x2 - x1
                for i in range(diff + 1):
                    self.grid[y1 - i][x1 + i] += 1
            elif x1 > x2 and y1 < y2: # SW diagonal
                diff = x1 - x2
                for i in range(diff + 1):
                    self.grid[y1 + i][x1 - i] += 1

    def print_vent_grid(self) -> None:
        ''' print out the vent grid in a nice manner '''
        for row in self.grid:
            for value in row:
                if value == 0:
                    print('.', end='')
                else:
                    print(value, end='')
            print('')

    def print_solution_1(self) -> None:
        ''' solution part 1 '''
        self.apply_straight_lines_to_grid()
        # self.print_vent_grid()
        solution = 0
        for row in self.grid:
            for value in row:
                if value >= 2:
                    solution += 1
        print(f'Part 1: {solution}')

    def print_solution_2(self) -> None:
        ''' solution part 2 '''
        self.apply_straight_lines_to_grid()
        self.apply_diagonal_lines_to_grid()
        # self.print_vent_grid()
        solution = 0
        for row in self.grid:
            for value in row:
                if value >= 2:
                    solution += 1
        print(f'Part 2: {solution}')

def part1():
    '''part1'''
    vent = Vent('/Users/laith/adventOfCode/2021/day/5/input.txt')
    vent.print_solution_1()

def part2():
    '''part2'''
    vent = Vent('/Users/laith/adventOfCode/2021/day/5/input.txt')
    vent.print_solution_2()

part1()
part2()
