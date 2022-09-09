# Problem: https://adventofcode.com/2021/day/4

class BingoValue:
    def __init__(self, value):
        self.value = value
        self.marked = False

class BingoBoard:
    def __init__(self, board):
        self.board = board
        self.hasWon = False
    
    def isWinner(self):
        # Check rows for a win
        for row in self.board:
            row_marked_values = list(map(lambda val: val.marked, row))
            if all(row_marked_values):
                return True
        
        # Check columns for a win
        for col_num in range(5):
            col_marked_values = [
                self.board[0][col_num].marked,
                self.board[1][col_num].marked,
                self.board[2][col_num].marked,
                self.board[3][col_num].marked,
                self.board[4][col_num].marked,
            ]
            if all(col_marked_values):
                return True
        
        return False

    def calculateFinalScore(self, draw):
        unmarkedSum = 0
        for row in self.board:
            for bingo_value in row:
                if not bingo_value.marked:
                    unmarkedSum += bingo_value.value
        return unmarkedSum * draw

        

def part1():
    inputFile = open('/Users/laith/adventOfCode/2021/day/4/input.txt')
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
                        if bingo_board.isWinner():
                            bingo_board.hasWon = True
                            print(f'part 1: {bingo_board.calculateFinalScore(draw)}')
                            inputFile.close()
                            return


def part2():
    inputFile = open('/Users/laith/adventOfCode/2021/day/4/input.txt')
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
                        if not bingo_board.hasWon and bingo_board.isWinner():
                            bingo_board.hasWon = True
                            print(f'part 2: {bingo_board.calculateFinalScore(draw)}')
    
    inputFile.close()

part1()
part2()
