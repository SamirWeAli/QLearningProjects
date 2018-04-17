
from src.game import *

import pygame

if __name__ == '__main__':
    game = Game()
    pygame.init()
    i = ITERATIONS_COUNT

    window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
    while i != 0:
        # Update pygame display(required).
        pygame.display.update()

        # Fill window.
        window.fill(WHITE)

        # Add some delay to see the drawing.
        pygame.time.delay(100)

        # Pass window parameter to draw player, hole and cheese
        game.draw(window)
        game.game_loop()

        if game.score > MAX_SCORE or game.score < MIN_SCORE:
            game.reset()
        i -= 1
