'''
Problem: https://adventofcode.com{PROBLEM_DAY}

 1 (2):  7 (3):   4 (4):   8 (7):   6 (6):   0 (6):   9 (6):
 ....    aaaa     ....     aaaa     aaaa     aaaa     aaaa
.    c  .    c   b    c   b    c   b    .   b    c   b    c
.    c  .    c   b    c   b    c   b    .   b    c   b    c
 ....    ....     dddd     dddd     dddd     ....     dddd
.    f  .    f   .    f   e    f   e    f   e    f   .    f
.    f  .    f   .    f   e    f   e    f   e    f   .    f
 ....    ....     ....     gggg     gggg     gggg     gggg

  2 (5):  3 (5):  5 (5):
  aaaa    aaaa    aaaa  
 .    c  .    c  b    . 
 .    c  .    c  b    . 
  dddd    dddd    dddd  
 e    .  .    f  .    f 
 e    .  .    f  .    f 
  gggg    gggg    gggg  
'''
PROBLEM_DAY = '/2021/day/8'

class Solution:
    ''' A class representing the solution for this problem '''
    def __init__(self, file_path, test=False) -> None:
        input_file = open(f"{file_path}{'/test.txt' if test else '/input.txt'}", encoding="utf-8")
        # Create list of entries which contains tuples of patterns list and values list
        self.entries = []
        for line in input_file:
            signal_pattern, output_value = line.split('|')
            patterns = signal_pattern.strip().split()
            values = output_value.strip().split()
            self.entries.append((patterns, values))

        unique_segment_values = {2, 3, 4, 7}
        self.unique_digit_count = 0
        for entry in self.entries:
            for value in entry[1]:
                if len(value) in unique_segment_values:
                    self.unique_digit_count += 1
        input_file.close()

def part_1(test=False) -> None:
    ''' solution part 1 '''
    solution = Solution(f'/Users/laith/adventOfCode{PROBLEM_DAY}', test)
    print('Part 1:')
    print(solution.unique_digit_count)

def part_2(test=False) -> None:
    ''' solution part 2 '''
    solution = Solution(f'/Users/laith/adventOfCode{PROBLEM_DAY}', test)
    print('\nPart 2:')
    values_to_sum = []
    for entry in solution.entries:
        digit_dict = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set(),
            9: set(),
        }
        segment_dict = {
            'top': '',
            'top_left': '',
            'top_right': '',
            'center': '',
            'bottom': '',
            'bottom_left': '',
            'bottom_right': ''
        }
        # We can automatically fill these in because they are unique
        digit_dict[1] = set(next(filter(lambda pattern: len(pattern) == 2, entry[0])))
        digit_dict[7] = set(next(filter(lambda pattern: len(pattern) == 3, entry[0])))
        digit_dict[4] = set(next(filter(lambda pattern: len(pattern) == 4, entry[0])))
        digit_dict[8] = set(next(filter(lambda pattern: len(pattern) == 7, entry[0])))

        # Top segment is the difference between the sets for 1 and 7
        segment_dict['top'] = ''.join(digit_dict[7] - digit_dict[1])

        # 6 is the only len 6 that does not contain 1
        digit_dict[6] = set(next(filter(lambda pattern: len(pattern) == 6 and not digit_dict[1].issubset(pattern), entry[0])))
        segment_dict['top_right'] = ''.join(digit_dict[8] - digit_dict[6])

        # 5 is the only one of len 5 that does not have top right
        digit_dict[5] = set(next(filter(lambda pattern: len(pattern) == 5 and not segment_dict['top_right'] in pattern, entry[0])))
        segment_dict['bottom_left'] = ''.join(digit_dict[6] - digit_dict[5])

        # 9 is only len 6 that contains the does not contain bottom left
        digit_dict[9] = set(next(filter(lambda pattern: len(pattern) == 6 and not segment_dict['bottom_left'] in pattern, entry[0])))
        
        # 0 is only len 6 that contains 1 and bottom left
        digit_dict[0] = set(next(filter(lambda pattern: len(pattern) == 6 and digit_dict[1].issubset(pattern) and segment_dict['bottom_left'] in pattern, entry[0])))
        segment_dict['center'] = ''.join(digit_dict[8] - digit_dict[0])

        # 3 is only len 5 that contains 1
        digit_dict[3] = set(next(filter(lambda pattern: len(pattern) == 5 and digit_dict[1].issubset(pattern), entry[0])))

        # 2 is only len 5 that has bottom left
        digit_dict[2] = set(next(filter(lambda pattern: len(pattern) == 5 and segment_dict['bottom_left'] in pattern, entry[0])))

        # lol
        output_frozen_sets = [frozenset(value) for value in entry[1]]
        frozen_digit_dict = {}
        for digit, digit_set in digit_dict.items():
            frozen_digit_dict[digit] = frozenset(digit_set)
        value_lookup = {v: k for k, v in frozen_digit_dict.items()}
        output_str = ''
        for output_set in output_frozen_sets:
            output_str += str(value_lookup[output_set])
        values_to_sum.append(int(output_str))
    print(sum(values_to_sum))

part_1()
part_2()

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
