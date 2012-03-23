import pygame
import os
import sys
from shoot_globals import *

bimages = [
     "images/ball_8.png",
     "images/ball_10.png",
     "images/ball_12.png",
     "images/ball_14.png",
     "images/ball_16.png",
     "images/ball_18.png",
     "images/ball_20.png",
     "images/ball_22.png",
     "images/ball_24.png",
     "images/ball_26.png",
     "images/ball_28.png",
     "images/ball_30.png",
     "images/ball_32.png"]
num_bimages = len(bimages)
steps = num_bimages - 1
class Bullet(pygame.sprite.Sprite):
    images = []
    images_loaded = False

    def __init__(self, screen, initialpos, targetpos, snd):
        pygame.sprite.Sprite.__init__(self)
        # Load all iamges
        if not Bullet.images_loaded:
            for str in bimages:
                Bullet.images.append(pygame.image.load(str).convert_alpha(screen))
            Bullet.images_loaded = True
            Bullet.snd = snd
        # Initialisation
        self.image = Bullet.images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = initialpos
        self.next_update_time = 0 
        self.next_image_time = 0 
        self.current_image = 0
        self.current_image_inc = 1
        self.snd = Bullet.snd

        # calculate increment so bullet lands in right place
        (self.posx, self.posy)=initialpos
        self.posx *= 1.0 # for accurate positioning
        self.posy *= 1.0
        (targetx, targety)=targetpos
        dist = math.sqrt((SHEIGHT-80-targety)*(SHEIGHT-80-targety)+targetx*targetx)
        self.maximage = num_bimages*dist/SCREENPLAYDIAG + 3
        if self.maximage >= num_bimages:
            self.maximage = num_bimages -1
        self.xinc=((targetx - self.posx)/(self.maximage*5.0))
        self.yinc=((targety - self.posy)/(self.maximage*5.0))

    def update(self, bullets, current_time):
        if self.next_update_time < current_time:
            if self.rect.top < BORDERWIDTH:
                bullets.remove(self)
                self.kill()
            self.posx += self.xinc # keep track of floating point position
            self.posy += self.yinc
            self.rect.left = self.posx # this will round to integer
            self.rect.top = self.posy
            self.next_update_time = current_time + 10

        if self.next_image_time < current_time:
            self.current_image += self.current_image_inc
            if self.current_image >= self.maximage:
                self.current_image_inc *= -1
                self.current_image += self.current_image_inc
            if self.current_image == 0:
                self.snd.play()
                self.kill()
            self.image = Bullet.images[self.current_image]
            self.next_image_time = current_time + 100


