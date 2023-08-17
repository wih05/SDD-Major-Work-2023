# Main File the handle the menus and maybe the battles, although they may be in different files.

#-- Imports --#
import pygame
import button
import os

#--         --#

#-- Setup --#
pygame.init()
clock = pygame.time.Clock()
FPS = 60

# Window dimensions
Screen_Height = 730
Screen_Width = 1200

# Window creation
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption('Kanji Fighters') # WIP name

# Text Setup
White = (255, 255, 255) # RGB value of white
Pixil_Font = pygame.font.SysFont('consolas', 30, True) # Font setup, Font: consolas, size 30, Bold

# load BG images
bg_images = []
for i in range(1,5): #goes through and loads every background and adds to a list
    bg_image = pygame.image.load(f"Program\Sprites\BG_img_{i}.png").convert_alpha()
    bg_image = pygame.transform.scale(bg_image, (1400, 730)) # scales image down by 3, (they are 3 times as big as the screen)
    bg_images.append(bg_image)
# Load images
Levels_img = pygame.image.load('Program\Sprites\Menu_Levels_Button.png').convert_alpha()
Endless_img = pygame.image.load('Program\Sprites\Menu_Endless_Button.png').convert_alpha()
Help_img = pygame.image.load('Program\Sprites\Menu_Help_Button.png').convert_alpha()
Quit_img = pygame.image.load('Program\Sprites\Menu_Quit_Button.png').convert_alpha()
Levels_S_img = pygame.image.load('Program\Sprites\Menu_Levels_Button_S.png').convert_alpha()
Endless_S_img = pygame.image.load('Program\Sprites\Menu_Endless_Button_S.png').convert_alpha()
Help_S_img = pygame.image.load('Program\Sprites\Menu_Help_Button_S.png').convert_alpha()
Menu_Text_BG = pygame.image.load('Program\Sprites\Menu_Text_BG.png').convert_alpha()
Menu_Text_BG = pygame.transform.scale(Menu_Text_BG, (900, 600)) # Scales IMG up by 2
MM_Play_img = pygame.image.load('Program\Sprites\MM_Play_Button.png').convert_alpha()
# Buttons
Levels_Button = button.Button(Levels_img, 2)
Endless_Button = button.Button(Endless_img, 2)
Help_Button = button.Button(Help_img, 2)
Quit_Button = button.Button(Quit_img, 2)
Levels_Button_S = button.Button(Levels_S_img, 2)
Endless_Button_S = button.Button(Endless_S_img, 2)
Help_Button_S = button.Button(Help_S_img, 2)
MM_Play_Button = button.Button(MM_Play_img, 2)


game_state = 'Main_Menu'

scroll = 5

goto = ''
#--       --#

#-- Functions --#
def Display_Text(Surface, Text, Font, Colour, x, y): # function to display text on screen
    text = Font.render(Text, True, Colour) # creates the text
    Surface.blit(text, (x, y)) # displays text

def draw_bg():
    for x in range(100):
        speed = 1
        for i in bg_images:
            screen.blit(i, ((x*1400) - scroll * speed, 0)) #what does the scroll
            speed += 0.2 
#--           --#
    
#-- Main Loop --#
run = True
while run:
    
    #draw bg
    draw_bg()
    if scroll <= 32400: #scrolls for 9 mins
        scroll += 1
    elif scroll <= 33000:
        scroll += 0.5 #slows down to half speed before stopping

    if game_state == 'Main_Menu': # Main menu screen
        if Levels_Button.draw(520, 100, screen):
            game_state = 'Levels'
        if Endless_Button.draw(520, 260, screen):
            game_state = 'Endless'
        if Help_Button.draw(520, 440, screen):
            game_state = 'Help'
        if Quit_Button.draw(520, 620, screen):
            run = False # Stops game loop, might add a 'are you sure?' question.
    
    if game_state == 'Levels':
        Levels_Button_S.draw(50, 100, screen)
        if Endless_Button.draw(50, 260, screen):
            game_state = 'Endless'
        if Help_Button.draw(50, 440, screen):
            game_state = 'Help'
        if Quit_Button.draw(50, 620, screen):
            run = False
        screen.blit(Menu_Text_BG, (250, 100))

    if game_state == 'Endless':
        if Levels_Button.draw(50, 100, screen):
            game_state = 'Levels'
        Endless_Button_S.draw(50, 260, screen)
        if Help_Button.draw(50, 440, screen):
            game_state = 'Help'
        if Quit_Button.draw(50, 620, screen):
            run = False
        screen.blit(Menu_Text_BG, (250, 100))
        if MM_Play_Button.draw(600, 150, screen):
            goto = 'Endless'
            run = False

    if game_state == 'Help':
        if Levels_Button.draw(50, 100, screen):
            game_state = 'Levels'
        if Endless_Button.draw(50, 260, screen):
            game_state = 'Endless'
        Help_Button_S.draw(50, 440, screen)
        if Quit_Button.draw(50, 620, screen):
            run = False
        screen.blit(Menu_Text_BG, (250, 100))
        Display_Text(screen, "Help:", Pixil_Font, White, 260, 105)
        Display_Text(screen, "To start select either 'Levels' or 'Endless'", Pixil_Font, White, 260, 140)
        Display_Text(screen, "from there select a level, or difficulty, then", Pixil_Font, White, 260, 170)
        Display_Text(screen, "press start and begin the battle.", Pixil_Font, White, 260, 195)
        Display_Text(screen, "In Battle Help:", Pixil_Font, White, 260, 255)
        Display_Text(screen, "In battle, to attack select an option from the", Pixil_Font, White, 260, 290)
        Display_Text(screen, "'attack' area, in order to deal damage however,", Pixil_Font, White, 260, 320)
        Display_Text(screen, "you must select the option correlating to the", Pixil_Font, White, 260, 350)
        Display_Text(screen, "enemy kanji. this may be either the correct readings", Pixil_Font, White, 260, 380)
        Display_Text(screen, "or definition of the kanji.", Pixil_Font, White, 260, 410)
        Display_Text(screen, "In some cases, the enemy kanji may have multiple", Pixil_Font, White, 260, 440)
        Display_Text(screen, "characters, to make up a word. In that case", Pixil_Font, White, 260, 470)
        Display_Text(screen, "the method of attack remains the same, using either", Pixil_Font, White, 260, 500)
        Display_Text(screen, "the reading of the kanji when in the word or", Pixil_Font, White, 260, 530)
        Display_Text(screen, "the definition of the word itself.", Pixil_Font, White, 260, 560)
        Display_Text(screen, "Finally once you finish, the next level will be", Pixil_Font, White, 260, 590)
        Display_Text(screen, "unlocked, or highscore added to 'Endless' screen.", Pixil_Font, White, 260, 620)
        Display_Text(screen, "Finally, have fun!", Pixil_Font, White, 260, 650)

    for event in pygame.event.get(): # Checks for event occuring
        
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update() # Updates display

pygame.quit() # Closes window... it quits.

if goto == 'Endless':
    os.system('Program\Endless.py')
