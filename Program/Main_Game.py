# Main File the handle the menus and maybe the battles, although they may be in different files.

#-- Imports --#
import pygame
import button

#--         --#

#-- Setup --#
# Window dimensions
Screen_Height = 730
Screen_Width = 1200

# Window creation
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption('Kanji Fighters') # WIP name

# Load images
Levels_img = pygame.image.load('Program\Sprites\Menu_Levels_Button.png').convert_alpha()
Endless_img = pygame.image.load('Program\Sprites\Menu_Endless_Button.png').convert_alpha()
Help_img = pygame.image.load('Program\Sprites\Menu_Help_Button.png').convert_alpha()
Quit_img = pygame.image.load('Program\Sprites\Menu_Quit_Button.png').convert_alpha()
Levels_S_img = pygame.image.load('Program\Sprites\Menu_Levels_Button_S.png').convert_alpha()
Endless_S_img = pygame.image.load('Program\Sprites\Menu_Endless_Button_S.png').convert_alpha()
Help_S_img = pygame.image.load('Program\Sprites\Menu_Help_Button_S.png').convert_alpha()
# Buttons
Levels_Button = button.Button(Levels_img, 2)
Endless_Button = button.Button(Endless_img, 2)
Help_Button = button.Button(Help_img, 2)
Quit_Button = button.Button(Quit_img, 2)
Levels_Button_S = button.Button(Levels_S_img, 2)
Endless_Button_S = button.Button(Endless_S_img, 2)
Help_Button_S = button.Button(Help_S_img, 2)


game_state = 'Main_Menu'

#-- Main Loop --#
run = True
while run:

    screen.fill((138, 189, 207)) #sets color to a light blue like color (placeholder for background)

    if game_state == 'Main_Menu': #main menu screen
        if Levels_Button.draw(520, 100, screen):
            game_state = 'Levels'
        if Endless_Button.draw(520, 260, screen):
            game_state = 'Endless'
        if Help_Button.draw(520, 440, screen):
            game_state = 'Help'
        if Quit_Button.draw(520, 620, screen):
            run = False # Stops game loop, might add an, 'are you sure?' question.
    
    if game_state == 'Levels':
        Levels_Button_S.draw(50, 100, screen)
        if Endless_Button.draw(50, 260, screen):
            game_state = 'Endless'
        if Help_Button.draw(50, 440, screen):
            game_state = 'Help'
        if Quit_Button.draw(50, 620, screen):
            run = False

    if game_state == 'Endless':
        if Levels_Button.draw(50, 100, screen):
            game_state = 'Levels'
        Endless_Button_S.draw(50, 260, screen)
        if Help_Button.draw(50, 440, screen):
            game_state = 'Help'
        if Quit_Button.draw(50, 620, screen):
            run = False

    if game_state == 'Help':
        if Levels_Button.draw(50, 100, screen):
            game_state = 'Levels'
        if Endless_Button.draw(50, 260, screen):
            game_state = 'Endless'
        Help_Button_S.draw(50, 440, screen)
        if Quit_Button.draw(50, 620, screen):
            run = False

    for event in pygame.event.get(): # Checks for event occuring
        
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update() # Updates display

pygame.quit() # Closes window... it quits.
