#-- imports --#
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
pygame.display.set_caption('Kanji Fighters: Endless') # WIP name

# Text Setup
White = (255, 255, 255) # RGB value of white
Black = (0, 0, 0)
Red = (255, 0, 0)
Pixil_Font = pygame.font.SysFont('consolas', 30, True) # Font setup, Font: consolas, size 30, Bold
Pixil_Font_Big = pygame.font.SysFont('consolas', 100, True)

# Load images
Exit_img = pygame.image.load('Program\Sprites\IG_Exit_Button.png').convert_alpha()
Retry_img = pygame.image.load('Program\Sprites\IG_Retry_Button.png').convert_alpha()

# Buttons
Exit_Button = button.Button(Exit_img, 2)
Retry_Button = button.Button(Retry_img, 2)


#-- variables --#
game_state = "Battle"
score = 0
health = 0
#--           --#

#-- functions --#
def Display_Text(Surface, Text, Font, Colour, x, y): # function to display text on screen
    text = Font.render(Text, True, Colour) # creates the text
    Surface.blit(text, (x, y)) # displays text
#--           --#
#-- Main Loop --#
run = True
while run:

    if game_state == 'Battle':
        screen.fill((138, 189, 207)) # sets color to a light blue like color (placeholder for background)
        if health > 0:
            # check if enemy is alive, if not spawn one
            print("True")
            #create the attacks based on the enemy

            #chose attack

            #if attack is correct, kill the enemy and increase score by one

            #if false, lose 1 health
        else:
            game_state = 'Death'

    if game_state == 'Death':
        screen.fill(Red) #sets colour to red
        Display_Text(screen, f"Score:  {score}", Pixil_Font, Black, 50, 50)
        Display_Text(screen, "You Died...", Pixil_Font_Big, Black, 350, 300)
        #maybe add a thing showing if highscore or not
        if Exit_Button.draw(50, 600, screen):
            run = False
            #goto Main_Menu.py
        if Retry_Button.draw(990, 600, screen):
            health = 5
            score= 0
            game_state = 'Battle'

    
    for event in pygame.event.get(): # Checks for event occuring
        
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update() # Updates display
