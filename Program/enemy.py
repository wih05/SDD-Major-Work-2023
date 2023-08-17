# Enemy class to be use throughout the program

#-- Imports --#
import pygame
from random import randint
from random import shuffle

#--         --#

#-- Enemy Class --#
class Enemy():
    def __init__(self, correct, incorrect, image, scale):
        #-- answer lists --#
        self.correct_a = []
        for i in correct:
            self.correct_a.append(i) #makes sure the answers are actually in a list
        self.incorrect_a = []
        for i in incorrect:
            self.incorrect_a.append(i)
        for i in self.incorrect_a: #checks to see where the correct answers are in the incorrect list
            if i in self.correct_a:
                for y in range(len(self.incorrect_a)):
                    if i == self.incorrect_a[y-1]:
                        del self.incorrect_a[y-1]     #removes the unwanted answers
        print(self.correct_a)
        print(self.incorrect_a)
        self.correct_a_num = 0
        self.possible_answers = []
        #--              --#

        #-- Sprite setup --#
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale))) # scales the image based on the scale mod
        self.rect = self.image.get_rect()
        #--              --#

    def draw(self, x, y, surface):
        self.rect.topleft = (x, y)

        # Draw Sprite on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def move_generation(self):
        shuffle(self.incorrect_a)
        self.correct_a_num = randint(1, 4) #decides pos of correct answer
        self.possible_answers = []
        # if correct answer in 1st pos
        if self.correct_a_num == 1:
            # correct answer
            self.possible_answers.append(self.correct_a[randint(0, (len(self.correct_a)-1))])

            #incorrect answers
            answer_list = []
            for i in range(3):
                a = True # re-enable while loop
                while a == True:
                    possible_answer = self.incorrect_a[randint(0, (len(self.incorrect_a)-1))]
                    print(f"answer loop {i}: {possible_answer}")
                    if possible_answer not in answer_list:            # makes sure there is no duplicates of possible answers
                        self.possible_answers.append(possible_answer)
                        answer_list.append(possible_answer)
                        print(answer_list)
                        a = False # break while loop
                    print("loop")
            print(" for loop {i}")
        # if correct answer in 2nd pos
        elif self.correct_a_num == 2:
            answer_list = []
            #incorrect answer 1
            possible_answer = self.incorrect_a[randint(0, (len(self.incorrect_a)-1))]
            self.possible_answers.append(possible_answer)
            answer_list.append(possible_answer)

            #correct answer
            self.possible_answers.append(self.correct_a[randint(0, (len(self.correct_a)-1))])

            #incorect answers 2 & 3
            for i in range(2):
                a = True
                while a == True:
                    possible_answer = self.incorrect_a[randint(0, (len(self.incorrect_a)-1))]
                    if possible_answer not in answer_list:
                        self.possible_answers.append(possible_answer)
                        answer_list.append(possible_answer)
                        a = False
                    print("loop")
        # if correct answer in 3rd pos
        elif self.correct_a_num == 3:
            answer_list = []
            #incorrect answers 1 & 2
            for i in range(2):
                a = True
                while a == True:
                    possible_answer = self.incorrect_a[randint(0, (len(self.incorrect_a)-1))]
                    if possible_answer not in answer_list:
                        self.possible_answers.append(possible_answer)
                        answer_list.append(possible_answer)
                        a = False
                    print("loop")

            #correct answer
            self.possible_answers.append(self.correct_a[randint(0, (len(self.correct_a)-1))])

            #incorrect answer 3
            a = True
            while a == True:
                possible_answer = self.incorrect_a[randint(0, (len(self.incorrect_a)-1))]
                if possible_answer not in answer_list:
                    self.possible_answers.append(possible_answer)
                    a = False    #note for log, this is where infinite loop occured, found by adding 'loop' flag
                print("loop")
        # if correct answer in 4th pos
        elif self.correct_a_num == 4:
            #incorrect answers
            answer_list = []
            for i in range(3):
                a = True
                while a == True:
                    possible_answer = self.incorrect_a[randint(0, (len(self.incorrect_a)-1))]
                    if possible_answer not in answer_list:
                        self.possible_answers.append(possible_answer)
                        answer_list.append(possible_answer)
                        a = False
                    print("loop")
            self.possible_answers.append(self.correct_a[randint(0, (len(self.correct_a)-1))])

        #displaying the possible answers is done in the main program using the button class

    def answer_check(self, chosen_answer_num):
        if chosen_answer_num == self.correct_a_num:
            return True #if answered correctly will return True, Action done in main program as uses will differ
        else:
            return False
