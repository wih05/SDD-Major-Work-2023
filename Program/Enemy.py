# Enemy class to be use throughout the program

#-- Imports --#
import pygame
from random import randint

#--         --#

#-- Enemy Class --#
class Enemy():
    def __init__(self, correct_a, incorrect_a, image, scale):
        #-- answer lists --#
        self.correct_a = correct_a
        index_for_removal = []
        self.incorrect_a = incorrect_a
        for x in range(len(correct_a)):                #--
            for i in range(len(incorrect_a)):             #
                if correct_a[x] == incorrect_a[i]:        #
                    index_for_removal.append(i)           # removes all the correct answers from the incorrect list, that way
        index_for_removal.sort()                          #  the same incorrect list can be used for every kanji, only needing to differ correct list
        for z in index_for_removal:                       #
            del self.incorrect_a[z]                    #--
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

            #correct answer
            self.possible_answers.append(self.correct_a[randint(0, (len(self.correct_a)-1))])

            #incorrect answer 3
            a = True
            while a == True:
                possible_answer = self.incorrect_a[randint(0, (len(self.incorrect_a)-1))]
                if possible_answer not in answer_list:
                    self.possible_answers.append(possible_answer)
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
            self.possible_answers.append(self.correct_a[randint(0, (len(self.correct_a)-1))])

        #displaying the possible answers is done in the main program using the button class

    def answer_check(self, chosen_answer_num):
        if chosen_answer_num == self.correct_a_num:
            return True #if answered correctly will return True, Action done in main program as uses will differ
        else:
            return False
