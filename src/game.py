import time
import os
import numpy as np
import pygame
import sys

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

    def draw(self, window):
        status = ""
        for i in range(MAX_POSITION + 1):
            if self.player.position == i:
                status += 'P'
                color = BLACK
            elif MIN_POSITION == i:
                status += 'O'
                color = BLUE
            elif MAX_POSITION == i:
                status += 'C'
                color = RED
            else:
                status += '#'
                color = WHITE

            rect = pygame.Rect(i * BLOCK_SIZE, 50, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(window, color, rect)

            # Add text label
            myfont = pygame.font.SysFont("monospace", 50)

            label_status = myfont.render(status, 1, BLACK)
            label_moves = myfont.render("Number of moves: " + str(self.moves_count), 1, BLACK)
            window.blit(label_status,(40, 100))
            window.blit(label_moves,(40, 200))

        if self.score == 5:
            print(status, " ", self.score, " Number of moves: ", self.moves_count)