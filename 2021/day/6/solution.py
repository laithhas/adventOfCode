""" Problem: https://adventofcode.com/2021/day/6 """
from collections import defaultdict

PROBLEM_DAY = "/2021/day/6"


class Solution:
    """A class representing the solution for this problem"""

    def __init__(self, input_file_path) -> None:
        input_file = open(input_file_path, encoding="utf-8")
        self.initial_state = list(map(int, input_file.readline().strip().split(",")))
        input_file.close()

    def age_population_dumb(self, num_days) -> None:
        """Age population of fish by number of days given"""
        fish_population = self.initial_state.copy()
        print(f"Initial state: {fish_population}")
        for i in range(1, num_days + 1):
            new_fish = []
            for index, fish in enumerate(fish_population):
                if fish == 0:
                    fish_population[index] = 6
                    new_fish.append(8)
                else:
                    fish_population[index] -= 1
            fish_population.extend(new_fish)
            if i == num_days:
                print(f"After {i} days: ({len(fish_population)} total)")

    def age_population_smart(self, num_days):
        """Age population of fish by number of days given... with a dict!"""
        start_population = self.initial_state.copy()
        fish_dict = defaultdict(int)
        for start_age in start_population:
            fish_dict[start_age] += 1
        print(f"Initial state: {dict(fish_dict)}")
        for i in range(1, num_days + 1):
            new_fish_dict = defaultdict(int)
            for fish_age, freq in fish_dict.items():
                if fish_age == 0:
                    new_fish_dict[6] += freq
                    new_fish_dict[8] = freq
                else:
                    new_fish_dict[fish_age - 1] += freq
            if i == num_days:
                final_fish_dict = dict(sorted(new_fish_dict.items()))
                total_num_fish = sum(new_fish_dict.values())
                print(f"After {i} days: {final_fish_dict} ({total_num_fish} total)")
            fish_dict = new_fish_dict

    def print_solution_1(self) -> None:
        """solution part 1"""
        print("Part 1:")
        self.age_population_dumb(80)

    def print_solution_2(self) -> None:
        """solution part 2"""
        print("\nPart 2:")
        self.age_population_smart(256)


solution = Solution(f"/Users/laith/adventOfCode{PROBLEM_DAY}/input.txt")
solution.print_solution_1()
solution.print_solution_2()

# ''' Problem: https://adventofcode.com{PROBLEM_DAY} '''
# PROBLEM_DAY = '/20xx/day/x'

# class Solution:
#     ''' A class representing the solution for this problem '''
#     def __init__(self, input_file_path) -> None:
#         input_file = open(input_file_path, encoding="utf-8")
#         input_file.close()

#     def print_solution_1(self) -> None:
#         ''' solution part 1 '''
#         print('Part 1:')

#     def print_solution_2(self) -> None:
#         ''' solution part 2 '''
#         print('\nPart 2:')

# solution = Solution(f'/Users/laith/adventOfCode{PROBLEM_DAY}/test.txt')
# solution.print_solution_1()
# solution.print_solution_2()
