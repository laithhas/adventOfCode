''' Problem: https://adventofcode.com/2023/day/2 '''
PROBLEM_DAY = '/2023/day/2'
AOC_ROOT_LOCATION = '/home/runner' # /Users/laith

class Solution:
  ''' A class representing the solution for this problem '''
  def __init__(self, file_path, test=False) -> None:
    with open(
      f"{file_path}{'/test.txt' if test else '/input.txt'}",
      encoding="utf-8"
    ) as input_file:
      self.lines = input_file.read().split("\n")
      print(*self.lines, sep="\n", end="")
      self.part_1 = 0
      self.part_2 = 0

def part_1(test=False) -> None:
  ''' solution part 1 '''
  solution = Solution(f'{AOC_ROOT_LOCATION}/adventOfCode{PROBLEM_DAY}', test)
  print('\nPart 1:')
  print(f'{solution.part_1}\n')

def part_2(test=False) -> None:
  ''' solution part 2 '''
  solution = Solution(f'{AOC_ROOT_LOCATION}/adventOfCode{PROBLEM_DAY}', test)
  print('\nPart 2:')
  print(f'{solution.part_2}\n')

part_1(True)
part_2(True)

"""
What did I learn from doing this problem?
- 
"""


# ''' Problem: https://adventofcode.com/20xx/day/x '''
# PROBLEM_DAY = '/20xx/day/x'
# AOC_ROOT_LOCATION = '/home/runner' # /Users/laith

# class Solution:
#   ''' A class representing the solution for this problem '''
#   def __init__(self, file_path, test=False) -> None:
#     with open(
#       f"{file_path}{'/test.txt' if test else '/input.txt'}",
#       encoding="utf-8"
#     ) as input_file:
#       self.lines = input_file.read().split("\n")
#       print(*self.lines, sep="\n", end="")
#       self.part_1 = 0
#       self.part_2 = 0

# def part_1(test=False) -> None:
#   ''' solution part 1 '''
#   solution = Solution(f'{AOC_ROOT_LOCATION}/adventOfCode{PROBLEM_DAY}', test)
#   print('\nPart 1:')
#   print(f'{solution.part_1}\n')

# def part_2(test=False) -> None:
#   ''' solution part 2 '''
#   solution = Solution(f'{AOC_ROOT_LOCATION}/adventOfCode{PROBLEM_DAY}', test)
#   print('\nPart 2:')
#   print(f'{solution.part_2}\n')

# part_1(True)
# part_2(True)

"""
What did I learn from doing this problem?
- 
"""