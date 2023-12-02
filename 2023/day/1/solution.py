''' Problem: https://adventofcode.com/2023/day/1 '''
PROBLEM_DAY = '/2023/day/1'
AOC_ROOT_LOCATION = '/home/runner' # /Users/laith

import re

class Solution:
    ''' A class representing the solution for this problem '''
    def __init__(self, file_path, test=False) -> None:
      with open(
        f"{file_path}{'/test.txt' if test else '/input.txt'}",
        encoding="utf-8"
      ) as input_file:
        self.lines = input_file.read().split("\n")
        digit_arrays = [
            [int(char) for char in line if char.isdigit()]
            for line in self.lines
        ]
        calibrations_list = [
          int(str(arr[0]) + str(arr[-1])) for arr in digit_arrays if len(arr) > 0
        ]
        self.part_1 = sum(calibrations_list)
        string_to_digit = {
          'zerone' : '01',
          'oneight' : '18',
          'twone' : '21',
          'threeight' : '38',
          'fiveight' : '58',
          'sevenine' : '79',
          'eightwo' : '82',
          'eighthree' : '83',
          'nineight' : '98',
          'zero': '0',
          'one': '1',
          'two': '2',
          'three': '3',
          'four': '4',
          'five': '5',
          'six': '6',
          'seven': '7',
          'eight': '8',
          'nine': '9',
        }

        regex_digit_names_group = '|'.join(string_to_digit.keys())

        string_to_digit_conversion_array = [
          re.sub(
            regex_digit_names_group, 
            lambda match: string_to_digit[match.group()],
            line
          )
          for line in self.lines
        ]
        digit_arrays_including_strings = [
          [int(char) for char in string if char.isdigit()]
          for string in string_to_digit_conversion_array
        ]
        calibrations_list_including_strings = [
          int(str(arr[0]) + str(arr[-1]))
          for arr in digit_arrays_including_strings
        ]
        self.part_2 = sum(calibrations_list_including_strings)

def part_1(test=False) -> None:
    ''' solution part 1 '''
    solution = Solution(f'{AOC_ROOT_LOCATION}/adventOfCode{PROBLEM_DAY}', test)
    print('\nPart 1:')
    print(solution.part_1)

def part_2(test=False) -> None:
    ''' solution part 2 '''
    solution = Solution(f'{AOC_ROOT_LOCATION}/adventOfCode{PROBLEM_DAY}', test)
    print('\nPart 2:')
    print(solution.part_2)

part_1(True)
part_2()

"""
What did I learn from doing this problem?
- How list comprehension works: [{transformation} {for x in y} {optional condition}]
  and these can be nested
- Regex groups using '|' (e.g. 'one|two|three|...|nine')
- Regex substitution using re.sub(regex, replacement, string)
- Dictionary hacks like string_to_digit = {'zerone' : '01', 'oneight' : '18', ...}
- https://chat.openai.com/share/c25314fa-3ae1-4677-a6c0-8ab20aace64b
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