''' Problem: https://adventofcode.com{PROBLEM_DAY} '''
PROBLEM_DAY = '/2021/day/9'

class Solution:
    ''' A class representing the solution for this problem '''
    def __init__(self, file_path, test=False) -> None:
        input_file = open(f"{file_path}{'/test.txt' if test else '/input.txt'}", encoding="utf-8")
        input_file.close()

def part_1(test=False) -> None:
    ''' solution part 1 '''
    solution = Solution(f'/Users/laith/adventOfCode{PROBLEM_DAY}', test)
    print('Part 1:')
    print(solution)

def part_2(test=False) -> None:
    ''' solution part 2 '''
    solution = Solution(f'/Users/laith/adventOfCode{PROBLEM_DAY}', test)
    print('\nPart 2:')
    print(solution)

part_1(True)
part_2(True)

# ''' Problem: https://adventofcode.com{PROBLEM_DAY} '''
# PROBLEM_DAY = '/20xx/day/x'

# class Solution:
#     ''' A class representing the solution for this problem '''
#     def __init__(self, file_path, test=False) -> None:
#         input_file = open(f"{file_path}{'/test.txt' if test else '/input.txt'}", encoding="utf-8")
#         input_file.close()

# def part_1(test=False) -> None:
#     ''' solution part 1 '''
#     solution = Solution(f'/Users/laith/adventOfCode{PROBLEM_DAY}', test)
#     print('Part 1:')
#     print(solution)

# def part_2(test=False) -> None:
#     ''' solution part 2 '''
#     solution = Solution(f'/Users/laith/adventOfCode{PROBLEM_DAY}', test)
#     print('\nPart 2:')
#     print(solution)

# part_1(True)
# part_2(True)
