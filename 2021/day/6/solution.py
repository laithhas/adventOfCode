''' Problem: https://adventofcode.com/2021/day/6 '''
PROBLEM_DAY = '/2021/day/6'

class Solution:
    ''' A class representing the solution for this problem '''
    def __init__(self, input_file_path) -> None:
        input_file = open(input_file_path, encoding="utf-8")
        self.start_ages = list(map(int, input_file.readline().strip().split(',')))
        input_file.close()

    def print_solution_1(self) -> None:
        ''' solution part 1 '''
        print(self.start_ages)

    def print_solution_2(self) -> None:
        ''' solution part 2 '''

solution = Solution(f'/Users/laith/adventOfCode{PROBLEM_DAY}/test.txt')
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

#     def print_solution_2(self) -> None:
#         ''' solution part 2 '''

# solution = Solution(f'/Users/laith/adventOfCode{PROBLEM_DAY}/test.txt')
# solution.print_solution_1()
# solution.print_solution_2()
