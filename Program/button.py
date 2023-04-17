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

    def draw(self, surface):
        # Draw Button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))