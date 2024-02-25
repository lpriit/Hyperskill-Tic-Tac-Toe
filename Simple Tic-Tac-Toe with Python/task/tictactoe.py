class TicTacToe:

    def __init__(self, board):
        self.test = None
        self.board = board
        self.x_wins = 0
        self.o_wins = 0
        self.coordinates = ''
        self.board_grid = []
        self.turn = 'X'

    def print_board(self):
        print('---------\n| {} {} {} |\n| {} {} {} |\n| {} {} {} |\n---------'.format(self.board[0], self.board[1],
                                                                                      self.board[2], self.board[3],
                                                                                      self.board[4], self.board[5],
                                                                                      self.board[6], self.board[7],
                                                                                      self.board[8]))

    def board_into_grid(self):
        self.board_grid = [self.board[:3], self.board[3:6], self.board[6:]]

    def get_diagonal(self, diag_number):
        """
        Gets diagonal contents
        :param diag_number: diagonal number from 0 to 1
        :return: diagonal contents
        """
        if diag_number == 0:
            return '{}{}{}'.format(self.board[0], self.board[4], self.board[8])
        elif diag_number == 1:
            return '{}{}{}'.format(self.board[2], self.board[4], self.board[6])

    def get_column(self, col_number):
        """
        Gets column contents
        :param col_number: column number from 0 to 2
        :return: column contents
        """
        return self.board[col_number::3]

    def get_row(self, row_number):
        """
        Gets row contents
        :param row_number: row number from 0 to 2
        :return: row contents
        """
        if row_number == 0:
            return self.board[0:3]
        elif row_number == 1:
            return self.board[3:6]
        elif row_number == 2:
            return self.board[6:9]

    def check_winner(self, line):
        if line == 'XXX':
            self.x_wins += 1
        elif line == 'OOO':
            self.o_wins += 1

    def game_state(self):
        self.x_wins = 0
        self.o_wins = 0
        for x in range(0, 3):
            self.check_winner(self.get_column(x))
        for x in range(0, 3):
            self.check_winner(self.get_row(x))
        for x in range(0, 2):
            self.check_winner(self.get_diagonal(x))
        if ((self.x_wins > 0 and self.o_wins > 0) or (self.board.count('X') - self.board.count('O') >= 2) or
                (self.board.count('O') - self.board.count('X') >= 2)):
            print('Impossible')
        elif self.x_wins == 0 and self.o_wins == 0 and self.board.count('_') > 0:
            # print('Game not finished')
            self.check_coordinates()
        elif self.x_wins == 0 and self.o_wins == 0 and self.board.count('_') == 0:
            print('Draw')
        elif self.x_wins == 1 and self.o_wins == 0:
            print('X wins')
        elif self.x_wins == 0 and self.o_wins == 1:
            print('O wins')

    def check_coordinates(self):
        split_xy = input().split(' ')
        try:
            x = int(split_xy[0])
            y = int(split_xy[1])
            if (1 <= x <= 3) and (1 <= y <= 3):
                self.check_cell(x - 1, y - 1)
            else:
                print('Coordinates should be from 1 to 3!')
                self.check_coordinates()
        except ValueError:
            print('You should enter numbers!')
            self.check_coordinates()

    def check_cell(self, x, y):
        self.board_into_grid()
        cell_value = self.board_grid[x][y]
        if cell_value == 'X' or cell_value == 'O':
            print('This cell is occupied! Choose another one!')
            self.check_coordinates()
        elif cell_value == '_':
            self.write_board(x, y)

    def write_board(self, x, y):
        # print(self.board_grid)
        new_board_row = ''
        for i in range(0, 3):
            if i == y:
                new_board_row += self.turn
                if self.turn == 'X':
                    self.turn = 'O'
                else:
                    self.turn = 'X'
            else:
                new_board_row += self.board_grid[x][i]
        self.board_grid[x] = new_board_row
        new_board = ''
        for line in self.board_grid:
            new_board += line
        self.board = new_board

        self.print_board()
        self.game_state()


tictactoe = TicTacToe('_________')
tictactoe.print_board()
tictactoe.check_coordinates()
