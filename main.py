import pygame
import random


#  Hangman Button Objects


#  Utility Functions


#  Hangman Animation Functions


#  Hangman Words in list


#  initialization of the pygame module
pygame.init()

#  Game settings
SCREENWIDTH = 800
SCREENHEIGHT = 640

#  Display Initialization
GAMESCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('Hang Man')

#  Game Variables anf load functions


#  Main game loop.
RUN = True
while RUN:

    #  Fill the screen with Black Color
    GAMESCREEN.fill((0, 0, 0))

    #  Pygame event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    #  Update the display screen
    pygame.display.update()


pygame.quit()