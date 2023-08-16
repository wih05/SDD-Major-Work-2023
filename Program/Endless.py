#-- imports --#
import pygame
import button
from enemy import Enemy
from random import randint
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
Green = (0, 255, 0)
Pixil_Font = pygame.font.SysFont('consolas', 30, True) # Font setup, Font: consolas, size 30, Bold
Pixil_Font_Big = pygame.font.SysFont('consolas', 100, True)

# Kanji Creation
answer_list = ["above", "aki", "autumn", "below", "book", "do", "eight", "fire", "five", "food",
              "four", "getsu", "go", "gold", "hachi", "hi", "hon", "ichi", "ka", "kin", "mizu", 
              "moku", "moon", "ni", "nichi", "one", "roku", "san", "shi", "shita", "six", "soil",
              "sui", "sun", "tabe", "three", "tsuki", "two", "uchi", "ue", "water", "wood", "yon"]

Water_img = pygame.image.load('Program\Sprites\Kanji_Sprites\Water_Kanji.png').convert_alpha()
Above_img = pygame.image.load('Program\Sprites\Kanji_Sprites\Above_Kanji.png').convert_alpha()
Kanji_List = [
    Enemy(["mizu", "water", "sui"], answer_list, Water_img, 3),
    Enemy(["ue", "above"], answer_list, Above_img, (1/4))
]

# Load images
Exit_img = pygame.image.load('Program\Sprites\IG_Exit_Button.png').convert_alpha()
Retry_img = pygame.image.load('Program\Sprites\IG_Retry_Button.png').convert_alpha()

# Buttons
Exit_Button = button.Button(Exit_img, 2)
Retry_Button = button.Button(Retry_img, 2)


#-- variables --#
game_state = "Battle"
score = 0
health = 5
#--           --#

#-- functions --#
def Display_Text(Surface, Text, Font, Colour, x, y): # function to display text on screen
    text = Font.render(Text, True, Colour) # creates the text
    Surface.blit(text, (x, y)) # displays text
#--           --#
#-- Main Loop --#
run = True
Kanji_Generated = False
while run:
    clock.tick(10)
    if game_state == 'Battle':
        screen.fill((138, 189, 207)) # sets color to a light blue like color (placeholder for background)
        if health > 0:
            if Kanji_Generated == False:
                # Active kanji choice
                Active = randint(0, (len(Kanji_List)-1))
                print(f"Active = {Active}")
                Kanji_List[Active].move_generation()

                # making buttons for possible answers
                count = 1
                for i in Kanji_List[Active].possible_answers:
                    if count == 1:
                        Img_1 = pygame.image.load(f'Program\Sprites\Answer_Sprites\{i}_answer.png').convert_alpha()
                        Attack_1 = button.Button(Img_1, 2)
                    elif count == 2:
                        Img_2 = pygame.image.load(f'Program\Sprites\Answer_Sprites\{i}_answer.png').convert_alpha()
                        Attack_2 = button.Button(Img_2, 2)
                    elif count == 3:
                        Img_3 = pygame.image.load(f'Program\Sprites\Answer_Sprites\{i}_answer.png').convert_alpha()
                        Attack_3 = button.Button(Img_3, 2)
                    elif count == 4:
                        Img_4 = pygame.image.load(f'Program\Sprites\Answer_Sprites\{i}_answer.png').convert_alpha()
                        Attack_4 = button.Button(Img_4, 2)
                    print(f"loop {count}: {i}")
                    count += 1
                print("Button Creation Complete")
                Kanji_Generated = True
            Kanji_List[Active].draw(850, 200, screen) # draw the kanji to 'fight'
            if Attack_1.draw(50, 400, screen):
                if Kanji_List[Active].answer_check(1):
                    score += 1
                    screen.fill(Green)
                    Kanji_Generated = False
                else:
                    health -= 1
                    screen.fill(Red)
                    Kanji_Generated = False

            if Attack_2.draw(50, 550, screen):
                if Kanji_List[Active].answer_check(2):
                    score += 1
                    screen.fill(Green)
                    Kanji_Generated = False
                else:
                    health -= 1
                    screen.fill(Red)
                    Kanji_Generated = False

            if Attack_3.draw(300, 400, screen):
                if Kanji_List[Active].answer_check(3):
                    score += 1
                    screen.fill(Green)
                    Kanji_Generated = False
                else:
                    health -= 1
                    screen.fill(Red)
                    Kanji_Generated = False

            if Attack_4.draw(300, 550, screen):
                if Kanji_List[Active].answer_check(4):
                    score += 1
                    screen.fill(Green)
                    Kanji_Generated = False
                else:
                    health -= 1
                    screen.fill(Red)
                    Kanji_Generated = False
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
