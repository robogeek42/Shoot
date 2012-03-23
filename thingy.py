import pygame
import random
from shoot_globals import *

class Thingy(pygame.sprite.Sprite):
    image = None
    #mask = None
    def __init__(self, screen, initialpos):
        pygame.sprite.Sprite.__init__(self)
        if Thingy.image is None:
            Thingy.image = pygame.image.load("images/man2.png").convert_alpha(screen)
        self.image = Thingy.image
        self.rect = self.image.get_rect()
        self.rect.topleft = initialpos
        self.next_update_time = 0 
        self.xinc=random.randint(1,5)-3
        self.yinc=random.randint(1,5)-3
        if self.xinc == 0 and self.yinc == 0:
            self.xinc = 1
            self.yinc = -1


    def update(self, current_time):
        # Update every 10 milliseconds = 1/100th of a second.
        if self.next_update_time < current_time:
            if self.rect.top > (SHEIGHT - LOWERBORDER - IH):
                self.yinc *= -1
            if self.rect.top < (BORDERWIDTH):
                self.yinc *= -1
            if self.rect.left > (SWIDTH - BORDERWIDTH - IW):
                self.xinc *= -1
            if self.rect.left < (BORDERWIDTH):
                self.xinc *= -1

            # Move our position 
            self.rect.left += self.xinc
            self.rect.top += self.yinc

            self.next_update_time = current_time + 10


