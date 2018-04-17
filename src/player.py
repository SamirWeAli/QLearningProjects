import numpy as np

from src.configs import *


class Player:
    def __init__(self):
        self.position = INITIAL_POSITION
        self.old_position = INITIAL_POSITION

        self.q_table = np.random.uniform(-1, 1, (12, 2))  # TODO

        self.possible_actions = PLAYER_POSSIBLE_ACTIONS
        self.action_taken_index = None

        self.epsilon = EPSILON

    def get_action(self):
        prob = np.random.rand(1)

        # Pick random action.
        if prob > self.epsilon:
            self.action_taken_index = np.random.randint(len(self.possible_actions))
        else:
            # Get the index of the action having highest reward in table.
            self.action_taken_index = np.argmax(self.q_table[self.position], axis=0)

        next_action = self.possible_actions[self.action_taken_index]

        return next_action

    def update_q_table(self, previous_game_score, new_game_score):
        reward = 0
        if previous_game_score > new_game_score:
            reward = -1
        elif new_game_score > previous_game_score:
            reward = 1

        # Update Q table.
        self.q_table[self.old_position][self.action_taken_index] += LEARNING_RATE * (
            reward + DISCOUNT_FACTOR * np.max(self.q_table[self.position]) -
            self.q_table[self.old_position][self.action_taken_index])

    def reset(self):
        self.position = INITIAL_POSITION
        self.old_position = INITIAL_POSITION

        self.action_taken_index = None