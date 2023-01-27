""" Problem: https://adventofcode.com/2022/day/1 """
import heapq


PROBLEM_DAY = "/2022/day/1"


class Solution:
    """A class representing the solution for this problem"""

    def __init__(self, file_path, test=False) -> None:
        input_file = open(
            f"{file_path}{'/test.txt' if test else '/input.txt'}", encoding="utf-8"
        )
        self.lines = input_file.read().split("\n")
        self.calorie_values = list(map(lambda s: int(s.strip() or 0), self.lines))
        self.elves = []
        curr_cal = 0
        for calorie in self.calorie_values:
            if calorie == 0:
                self.elves.append(curr_cal)
                curr_cal = 0
            else:
                curr_cal += calorie
        input_file.close()


def part_1(test=False) -> None:
    """solution part 1"""
    solution = Solution(f"/Users/laith/adventOfCode{PROBLEM_DAY}", test)
    print("Part 1:")
    print(max(solution.elves))


def part_2(test=False) -> None:
    """solution part 2"""
    solution = Solution(f"/Users/laith/adventOfCode{PROBLEM_DAY}", test)
    print("\nPart 2:")
    print(sum(heapq.nlargest(3, solution.elves)))


part_1()
part_2()

# ''' Problem: https://adventofcode.com{PROBLEM_DAY} '''
# PROBLEM_DAY = '/20xx/day/x'

# class Solution:
#     ''' A class representing the solution for this problem '''
#     def __init__(self, file_path, test=False) -> None:
#         input_file = open(f"{file_path}{'/test.txt' if test else '/input.txt'}", encoding="utf-8")
#         self.lines = input_file.read().split("\n")
#         print(*self.lines, sep="\n", end="")
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

"""
What did I learn from doing this problem?
- What variadic arguments are and how unpacking works in python using * (https://medium.com/understand-the-python/understanding-the-asterisk-of-python-8b9daaa4a558)
- how to use heapq nlargest/nsmallest (https://note.nkmk.me/en/python-max-min-heapq-nlargest-nsmallest/)
"""
