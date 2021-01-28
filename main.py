import random
from Game import Game
GAME_LENGTH = 21

#game = Game()
#for i in range(GAME_LENGTH):
#    color = raw_input('Choose: "Y", "G", "B", "R": \r\n')
#    game.play(color)


def test():
    random.seed(0)
    game = Game()
    game.play("b")
    game.play("r")
    game.play("y")
    game.play("r")
    game.play("b")
    game.play("g")
    game.play("r")
    game.play("y")
    game.play("g")
    game.play("b")
    game.play("g")
    game.play("y")
    game.play("r")
    game.play("b")
    game.play("g")
    game.play("y")
    game.play("r")
    game.play("b")

test()



