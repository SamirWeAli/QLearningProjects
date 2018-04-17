from src.game import *

if __name__ == '__main__':
    game = Game()

    i = ITERATIONS_COUNT

    while i != 0:
        game.draw()

        game.game_loop()

        if game.score == MAX_SCORE or game.score == MIN_SCORE:
            game.reset()

        i -= 1
