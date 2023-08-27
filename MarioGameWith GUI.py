# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 00:08:20 2023

@author: shara
"""

import pygame
import random
import time

def a_star_algorithm(start, goal):
# Initialize Pygame
 pygame.init()

# Set up the display
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Mario Game')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Load images
mario_img = pygame.image.load('C:/Users/shara/OneDrive/Desktop/Machine learning/mario.jpg')  # Place an image of Mario in the same folder as your script
obstacle_img = pygame.image.load('C:/Users/shara/OneDrive/Desktop/Machine learning/obsM.jpg')  # Place an image of the obstacle in the same folder

# Get image dimensions
mario_width = 50
obstacle_width = 50

# Initial positions
player_position = (display_width // 2, display_height - mario_width)
obstacle_position = (display_width, display_height - obstacle_width - 50)

# Game loop
clock = pygame.time.Clock()
game_over = False

while not game_over:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
   
    # Clear the screen
    game_display.fill(black)
    
    # Display Mario and obstacle
    # AI-controlled Mario
    ai_move = a_star_algorithm(player_position, obstacle_position)
    if ai_move == 'L' and player_position[0] > 0:
        player_position = (player_position[0] - mario_width, player_position[1])
    elif ai_move == 'R' and player_position[0] < display_width - mario_width:
        player_position = (player_position[0] + mario_width, player_position[1])

    game_display.blit(mario_img, player_position)
    game_display.blit(obstacle_img, obstacle_position)
    
    pygame.display.update()
    
    # Check for collision
    if obstacle_position[0] < player_position[0] + mario_width and obstacle_position[0] + obstacle_width > player_position[0]:
        if obstacle_position[1] + obstacle_width > player_position[1]:
            game_over = True
    
    # Move the obstacle
    obstacle_position = (obstacle_position[0] - 5, obstacle_position[1])
    
    # Generate a new obstacle
    if obstacle_position[0] <= 0:
        obstacle_position = (display_width, display_height - obstacle_width - 50)
        time.sleep(1)
    
    clock.tick(30)

pygame.quit()
quit()
