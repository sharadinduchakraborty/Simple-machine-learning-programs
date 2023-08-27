# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 00:05:34 2023

@author: shara
"""

import random
import time

# Define the player and obstacles
player_position = 5
obstacle_position = 20

# Main game loop
while True:
    # Clear the screen
    print("\033[H\033[J")
    
    # Display the game
    game_display = [' '] * 40
    game_display[player_position] = 'M'
    game_display[obstacle_position] = 'X'
    
    print(''.join(game_display))
    
    # Check for collision
    if player_position == obstacle_position:
        print("Game Over!")
        break
    
    # Move the player and obstacle
    player_move = input("Move left (L) or right (R)? ").upper()
    
    if player_move == 'L' and player_position > 0:
        player_position -= 1
    elif player_move == 'R' and player_position < 39:
        player_position += 1
    
    obstacle_position -= 1
    
    # Generate a new obstacle
    if obstacle_position <= 0:
        obstacle_position = 40
        time.sleep(1)  # Delay to make the game playable
    
    # Add delay to control game speed
    time.sleep(0.1)
