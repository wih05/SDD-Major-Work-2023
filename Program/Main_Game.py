# Main File the handle the menus and maybe the battles, although they may be in different files.

#-- Imports --#
import pygame
import button

#--         --#

#-- Setup --#
# Window dimensions
Screen_Height = 750
Screen_Width = 1200

# Window creation
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption('Kanji Fighters') # WIP name

# Load images
Levels_img = pygame.image.load('Program\Sprites\Menu_Levels_Button.png').convert_alpha()
Endless_img = pygame.image.load('Program\Sprites\Menu_Levels_Button.png').convert_alpha()
Help_img = pygame.image.load('Program\Sprites\Menu_Help_Button.png').convert_alpha()
Quit_img = pygame.image.load('Program\Sprites\Menu_Quit_Button.png').convert_alpha()

# Buttons
Levels_Button = button.Button(520, 100,Levels_img, 2)
Endless_Button = button.Button(520, 280,Endless_img, 2)
Help_Button = button.Button(520, 460,Help_img, 2)
Quit_Button = button.Button(520, 640,Quit_img, 2)

#-- Main Loop --#
run = True
while run:

    if Levels_Button.draw(screen):
        print('Goto Levels')
    if Endless_Button.draw(screen):
        print('Goto Endless')
    if Help_Button.draw(screen):
        print('Goto Help')
    if Quit_Button.draw(screen):
        run = False # Stops game loop, might add an, 'are you sure?' question.

    for event in pygame.event.get(): # Checks for event occuring
        
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update() # Updates display

pygame.quit() # Closes window... it quits.