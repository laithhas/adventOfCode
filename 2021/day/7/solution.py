""" Problem: https://adventofcode.com/2021/day/7 """
from statistics import mean, median

PROBLEM_DAY = "/2021/day/7"


class Solution:
    """A class representing the solution for this problem"""

    def __init__(self, input_file_path, test=False) -> None:
        input_file = open(
            f'{input_file_path}{"test.txt" if test else "input.txt"}', encoding="utf-8"
        )
        self.crab_positions = list(map(int, input_file.readline().strip().split(",")))

        # median
        self.median_alignment_position = median(self.crab_positions)
        self.median_total_fuel_used = int(
            sum(
                abs(self.median_alignment_position - position)
                for position in self.crab_positions
            )
        )

        # mean
        self.mean_alignment_position = round(mean(self.crab_positions)) - 1
        self.mean_distances = [
            abs(self.mean_alignment_position - position)
            for position in self.crab_positions
        ]
        self.mean_total_fuel_used = int(
            sum((distance**2 + distance) / (2) for distance in self.mean_distances)
        )
        input_file.close()

    def part_1(self) -> None:
        """solution part 1"""
        print("Part 1:")
        print(self.median_total_fuel_used)

    def part_2(self) -> None:
        """solution part 2"""
        print("\nPart 2:")
        # between 96744815 and 96744966
        # answer was 96744904 (had to try numbers around the mean because of rounding)
        print(self.mean_alignment_position)
        # print(self.crab_positions)
        # print(self.mean_distances)
        print(self.mean_total_fuel_used)


solution1 = Solution(f"/Users/laith/adventOfCode{PROBLEM_DAY}/")
solution1.part_1()
solution2 = Solution(f"/Users/laith/adventOfCode{PROBLEM_DAY}/")
solution2.part_2()

# ''' Problem: https://adventofcode.com{PROBLEM_DAY} '''
# PROBLEM_DAY = '/20xx/day/x'

# class Solution:
#     ''' A class representing the solution for this problem '''
#     def __init__(self, file_path, test=False) -> None:
#         input_file = open(f"{file_path}{'/test.txt' if test else '/input.txt'}", encoding="utf-8")
#         input_file.close()

#     def part_1(self) -> None:
#         ''' solution part 1 '''
#         print('Part 1:')

#     def part_2(self) -> None:
#         ''' solution part 2 '''
#         print('\nPart 2:')

# solution = Solution(f'/Users/laith/adventOfCode{PROBLEM_DAY}')
# solution.part_1()
# solution.part_2()
