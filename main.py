import pygame
import random


#  Hangman Button Objects


#  Utility Functions
def openFile():
    """Open and load words from the text file into a simple list"""
    with open('easyWordList.txt', 'r') as file:
        content = file.readlines()
        newList = []
        for itemList in content:
            newList.append(itemList.split(','))

        for wordList in newList:
            for word in wordList:
                if len(word.strip()) >= 3 and len(word.strip()) <= 10:
                    WORDLIST.append(word.strip())


#  Hangman Animation Functions
def drawGallows(window):
    """Draw the Gallows"""
    pygame.draw.line(window, WHITE, (100, 400), (275, 400), 3)
    pygame.draw.line(window, WHITE, (125, 400), (125, 50), 3)
    pygame.draw.line(window, WHITE, (125, 50), (275, 50), 3)
    pygame.draw.line(window, WHITE, (125, 100), (175, 50), 3)
    pygame.draw.line(window, WHITE, (275, 50), (275, 125), 3)


def drawHead(window):
    """Draws the Hanged man's Head"""
    pygame.draw.circle(window, WHITE, (275, 150), (25), 3)


def drawBody(window):
    """Draws the Hanged Man's Body"""
    pygame.draw.line(window, WHITE, (275, 175), (275, 225), 3)


def drawLeftArm(window):
    """Draws the Hanged Man's Left Arm"""
    pygame.draw.line(window, WHITE, (275, 185), (245, 215), 3)


def drawRightArm(window):
    """Draws the Hanged Man's Right Arm"""
    pygame.draw.line(window, WHITE, (275, 185), (305, 215), 3)


def drawLeftLeg(window):
    """Draws the Hanged Man's Left Leg"""
    pygame.draw.line(window, WHITE, (275, 225), (250, 250), 3)
    pygame.draw.line(window, WHITE, (250, 250), (250, 275), 3)
    pygame.draw.line(window, WHITE, (250, 275), (240, 275), 3)


def drawRightLeg(window):
    """Draws the Hanged Man's Left Leg"""
    pygame.draw.line(window, WHITE, (275, 225), (300, 250), 3)
    pygame.draw.line(window, WHITE, (300, 250), (300, 275), 3)
    pygame.draw.line(window, WHITE, (300, 275), (310, 275), 3)


def drawHangman(window, numberGuesses):
    """Draws the various stages of the Hanged Man"""
    if numberGuesses >= 0:
        drawGallows(window)
    if numberGuesses >= 1:
        drawHead(window)
    if numberGuesses >= 2:
        drawBody(window)
    if numberGuesses >= 3:
        drawLeftArm(window)
    if numberGuesses >= 4:
        drawRightArm(window)
    if numberGuesses >= 5:
        drawLeftLeg(window)
    if numberGuesses >= 6:
        drawRightLeg(window)


#  Hangman Words list
WORDLIST = []
openFile()

#  initialization of the pygame module
pygame.init()

#  Game settings
SCREENWIDTH = 800
SCREENHEIGHT = 640
WHITE = (255, 255, 255)

#  Display Initialization
GAMESCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('Hang Man')

#  Game Variables anf load functions
numberOfGuesses = 3

#  Main game loop.
RUN = True
while RUN:

    #  Fill the screen with Black Color
    GAMESCREEN.fill((0, 0, 0))

    #  Pygame event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    drawHangman(GAMESCREEN, numberOfGuesses)

    #  Update the display screen
    pygame.display.update()


pygame.quit()