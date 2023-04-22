# Test file, with a basic screen that can be adjusted in order to test modules

#-- imports --#
import pygame

#--         --#

#-- Setup --#
# Window dimensions
Screen_Height = 500
Screen_Width = 800

# Window creation
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption('TEST WINDOW')

#-- Main Loop --#
run = True
while run:

    for event in pygame.event.get(): # Checks for event occuring
        
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update() # Updates display

pygame.quit() # Closes window... it quits.