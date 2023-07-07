#Imports
import pygame, random
from pygame import mixer
from pygame.locals import *
from time import sleep


#Global variables
screen_width = 800
screen_height = 800
SPEED = 8
GRAVITY = 0.8
player_speed = 17


#Setting up the game
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer Game')
game_over = False
player_image = pygame.image.load('x.png').convert()
player_image = pygame.transform.scale(player_image, (60, 60))
player_rect = player_image.get_rect()
player_rect.x = screen_width / 2
player_rect.y = screen_height / 2


#Game loop
while not game_over: 
    if player_rect.y >= (screen_height) - 50:
        game_over = True        
    #Main events loop
    for event in pygame.event.get():
        #If player closes window
        if event.type == pygame.QUIT:
            game_over = True
        #Arrow key movements
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_rect.x -= player_speed
            if event.key == pygame.K_RIGHT:
                player_rect.x += player_speed
            if event.key == pygame.K_UP:
                player_rect.y -= player_speed
            if event.key == pygame.K_DOWN:
                player_rect.y += player_speed

    #Game logic

    #Drawing logic   
    screen.fill((64, 224, 208))
    screen.blit(player_image, player_rect)

    #Update display
    pygame.display.flip()

#Quit game
pygame.quit()

