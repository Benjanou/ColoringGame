import random
from colorama import Back


class Tile:

    COLOR_OPTIONS = {"Y", "R", "G", "B"}

    def __init__(self, color):
        self.color = None
        self.set_color(color)
        self.visited = False

    def __str__(self):
        return self.color

    def set_color(self, color):
        if color in self.COLOR_OPTIONS:
            self.color = color
        self.visited = True

    def get_color(self):
        return self.color

    def set_visited(self):
        self.visited = False

    def get_visited(self):
        return self.visited


class Board:
    def __init__(self, height=18, width=18):
        self.height = height
        self.width = width
        self.board = self.create_board()

    def __str__(self):
        output = ""
        for i in range(self.height):
            for j in range(self.width):
                curr_color = self.board[i][j]
                output = output + " " + str(curr_color)
            output = output + " " + " \r\n"
        return output

    def create_board(self):
        board = []
        options = Tile.COLOR_OPTIONS
        for i in range(self.height):
            row = []
            for j in range(self.width):
                rand_color = random.choice(list(options))
                row.append(Tile(rand_color))
            board.append(row)
        return board

    def change_color(self, color):
        origin = self.board[0][0]
        curr_color = origin.get_color()
        self._initialize_visits()
        self._change_color(curr_color, color, 0, 0)

    def _change_color(self, original_col, color, col, row):
        if (col < self.width) and (row < self.height):
            curr_tile = self.board[row][col]
            if (curr_tile.get_color() == original_col) and (curr_tile.get_visited() is False):
                curr_tile.set_color(color)

                # checking neighbors
                # right
                if col+1 < self.width:
                    self._change_color(original_col, color, col+1, row)
                # down
                if row+1 < self.height:
                    self._change_color(original_col, color, col, row+1)

                # left
                if col-1 >= 0:
                    self._change_color(original_col, color, col - 1, row)
                # up
                if row-1 >= 0:
                    self._change_color(original_col, color, col, row - 1)

    def _initialize_visits(self):
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j].set_visited()

    def has_won(self):
        origin = self.board[0][0].get_color()
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j].get_color() != origin:
                    return False
        return True

    def get_board(self):
        return self.board












