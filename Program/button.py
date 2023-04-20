# button class for use within the rest of the program.

#-- imports --#
import pygame

#--         --#

#-- Button Class --#
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale))) # scales the image based on the scale mod
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        # Mouse position
        pos = pygame.mouse.get_pos()

        # Draw Button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        # Checks if mouse over button & checks for cliked button.
        if self.rect.collidepoint(pos): # checks if the mouse pos is within the buttons "hit box"
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #checks if button has been clicked while also preventing a new "click" while the button is held down
                self.clicked = True
                action = True # allows the 'action' to be dealt with in the main code.
                print("CLICKED")

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False # when no longer holding down left click, it turns clicked to false, allowing for another click
        return action