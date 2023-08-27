# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 22:23:45 2023

@author: shara
"""

import tkinter as tk
import numpy as np
import random

# Q-learning constants
LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.9
EXPLORATION_PROB = 0.1

class TicTacToeGUI:
    def __init__(self, root, q_table=None):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    root,
                    text=" ",
                    font=("Helvetica", 24),
                    width=6,
                    height=2,
                    command=lambda row=i, col=j: self.on_button_click(row, col),
                )
                self.buttons[i][j].grid(row=i, column=j)

        self.q_table = q_table if q_table is not None else {}
        self.state = self.get_state()
        self.previous_action = None

    def on_button_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            self.state = self.get_state()

            if self.check_winner(self.current_player):
                self.show_winner_message(self.current_player)
                self.reset_board()
            elif self.is_board_full():
                self.show_draw_message()
                self.reset_board()
            else:
                self.current_player = "X" if self.current_player == "O" else "O"
                if self.current_player == "O":
                    self.perform_ai_move()

    def perform_ai_move(self):
        if self.previous_action is not None:
            self.update_q_table(self.previous_action)

        if random.uniform(0, 1) < EXPLORATION_PROB:
            available_actions = self.get_available_actions()
            action = random.choice(available_actions)
        else:
            action = self.choose_best_action()

        row, col = action
        self.previous_action = action
        self.on_button_click(row, col)

    def choose_best_action(self):
        available_actions = self.get_available_actions()
        best_action = None
        best_value = -float("inf")

        for action in available_actions:
            value = self.q_table.get((self.state, action), 0)
            if value > best_value:
                best_value = value
                best_action = action

        return best_action

    def update_q_table(self, action):
        state_action = (self.state, action)
        reward = self.get_reward(self.current_player)
        future_rewards = [self.q_table.get((self.state, a), 0) for a in self.get_available_actions()]
        max_future_reward = max(future_rewards) if future_rewards else 0

        self.q_table[state_action] = (1 - LEARNING_RATE) * self.q_table.get(state_action, 0) + \
            LEARNING_RATE * (reward + DISCOUNT_FACTOR * max_future_reward)

    # Other methods (check_winner, is_board_full, get_state, get_available_actions, get_reward) remain unchanged...

def main():
    root = tk.Tk()
    q_table = {}  # You can load a pre-trained Q-table here if available
    app = TicTacToeGUI(root, q_table)
    root.mainloop()

if __name__ == "__main__":
    main()
