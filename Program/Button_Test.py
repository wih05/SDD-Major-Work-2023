# Test file, with a basic screen that can be adjusted in order to test modules

#-- imports --#
import pygame
import button

#--         --#

#-- Setup --#
# Window dimensions
Screen_Height = 500
Screen_Width = 800

# Window creation
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption('TEST WINDOW')

# load in Images
start_img = pygame.image.load('Program\Sprites\Start_Button.png').convert_alpha()
stop_img = pygame.image.load('Program\Sprites\Stop_Button.png').convert_alpha()

# Button Instances
start_button = button.Button(100, 200, start_img, 1)
stop_button = button.Button(450, 200, stop_img, 1)

#-- Main Loop --#
run = True
while run:

    if start_button.draw(screen): # checks if button has been clicked (done within class)
        print('Start')
    if stop_button.draw(screen):
        print('Stop')

    for event in pygame.event.get(): # Checks for event occuring
        
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update() # Updates display

pygame.quit() # Closes window... it quits.