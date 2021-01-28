from Board import Board, Tile
from colorama import Back

class Game:
    def __init__(self, turns=21, height=18, width=18):
        self.turns = turns
        self.board = Board(height, width)
        self.ui = UI(self.board)
        self.message()


    def play(self, color):
        if self.turns > 1:
            self._play(color)
        elif self.turns == 1:
            self._play(color)
            print "Game Over"
        else:
            print "Game is Over"

    def _play(self, color):
        self.turns = self.turns - 1
        color = color.upper()
        self.board.change_color(color)
        if self.board.has_won():
            print("you made it with {} left".format(self.turns))
            self.ui.str_board()
        else:
            self.message()

    def message(self):
        print("turns: {}".format(self.turns))
        self.ui.str_board()


class UI:
    def __init__(self, board):
        self.board = board

    def str_tile(self, tile):
        color_map = {"Y": Back.YELLOW,
                     "G": Back.GREEN,
                     "B": Back.BLUE,
                     "R": Back.RED}
        for i in color_map:
            if i == tile.get_color():
                return color_map[i] + i

    def str_board(self):
        output = ""
        for i in range(self.board.height):
            for j in range(self.board.width):
                curr_color = self.board.get_board()[i][j]
                output = output + " " + self.str_tile(curr_color)
            output = output + " " + Back.RESET + " \r\n"
        print(output)

