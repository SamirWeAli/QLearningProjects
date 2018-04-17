from asyncio import sleep

import numpy as np
import src.player as player
from src.configs import *


class Game:
    def __init__(self):
        self.player = player.Player()

        self.reset()

    def game_loop(self):
        self.moves_count += 1

        action = self.player.get_action()

        previous_game_score = self.score

        self.player.old_position = self.player.position

        self.player.position += action
        self.player.position = max(MIN_POSITION, self.player.position)
        self.player.position = min(MAX_POSITION, self.player.position)

        if self.player.position == CHEESE_POSITION:
            self.score += 1
        elif self.player.position == PIT_POSITION:
            self.score -= 1

        # Update Q table.
        self.player.update_q_table(previous_game_score, self.score)

    def reset(self):
        # Cheese position.
        self.cheese_position = CHEESE_POSITION

        # Pit (hole) position.
        self.pit_position = PIT_POSITION

        # Create a single player.
        self.player.reset()

        self.score = 0
        self.moves_count = 0

    def draw(self):
        status = ""
        for i in range(MAX_POSITION + 1):
            if self.player.position == i:
                status += 'P'
            elif MIN_POSITION == i:
                status += 'O'
            elif MAX_POSITION == i:
                status += 'C'
            else:
                status += '#'
        if self.score == 5:
            print(status, " ", self.score, " Number of moves: ", self.moves_count)
        sleep(500)
