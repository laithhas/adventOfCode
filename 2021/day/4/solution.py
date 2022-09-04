class BingoValue:
    def __init__(self, value):
        self.value = value
        self.marked = False

class BingoBoard:
    def __init__(self, board):
        self.board = board

def part1():
    inputFile = open('/Users/laith/adventOfCode/2021/day/4/test.txt')
    # Parses first line of input into a list of ints
    list_of_draws = list(map(int, inputFile.readline().strip().split(',')))

    board_string = ''
    for line in inputFile:
        board_string += line

    board_list = board_string.split('\n')

    bingo_board_list = []
    curr_bingo_board = []
    for board_row in board_list:
        if board_row  == '':
            curr_bingo_board = []
        else:
            board_row_list = list(map(int, board_row.strip().split()))
            bingo_values_list = list(map(lambda value: BingoValue(value), board_row_list))

            curr_bingo_board.append(bingo_values_list)
            if len(curr_bingo_board) == 5:
                bingo_board_list.append(curr_bingo_board)

    board_objects = []
    for board in bingo_board_list:
        board_objects.append(BingoBoard(board))

    # Iterates over draws and marks values that are called across all boards
    for draw in list_of_draws:
        for bingo_board in board_objects:
            for value_list in bingo_board.board:
                for bingo_value in value_list:
                    if bingo_value.value == draw:
                        bingo_value.marked = True

                        # Up next: need to check if bingo has been achieved
                        # on any board and stop iterating/calculate final score

    inputFile.close()

def part2():
    inputFile = open('/Users/laith/adventOfCode/2021/day/4/input.txt')
    # for line in inputFile:
    #     print('')
    inputFile.close()

part1()
part2()