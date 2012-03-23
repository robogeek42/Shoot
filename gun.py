import pygame
from shoot_globals import *

gimages = [
    "images/gun/gun_280.png",
    "images/gun/gun_285.png",
    "images/gun/gun_290.png",
    "images/gun/gun_295.png",
    "images/gun/gun_300.png",
    "images/gun/gun_305.png",
    "images/gun/gun_310.png",
    "images/gun/gun_315.png",
    "images/gun/gun_320.png",
    "images/gun/gun_325.png",
    "images/gun/gun_330.png",
    "images/gun/gun_335.png",
    "images/gun/gun_340.png",
    "images/gun/gun_345.png",
    "images/gun/gun_350.png",
    "images/gun/gun_355.png",
    "images/gun/gun_0.png",
    "images/gun/gun_5.png",
    "images/gun/gun_10.png",
    "images/gun/gun_15.png",
    "images/gun/gun_20.png",
    "images/gun/gun_25.png",
    "images/gun/gun_30.png",
    "images/gun/gun_35.png",
    "images/gun/gun_40.png",
    "images/gun/gun_45.png",
    "images/gun/gun_50.png",
    "images/gun/gun_55.png",
    "images/gun/gun_60.png",
    "images/gun/gun_65.png",
    "images/gun/gun_70.png",
    "images/gun/gun_75.png",
    "images/gun/gun_80.png"]

launchpos = [
    (50,1), # 0
    (55,1), # 5
    (60,2), # 10
    (64,2), # 15
    (68,3), # 20
    (72,4), # 25
    (75,6), # 30
    (78,9), # 35
    (81,13), # 40
    (84,16), # 45
    (88,20), # 50
    (85,24), # 55
    (86,28), # 60
    (88,32), # 65
    (90,36), # 70
    (93,39), # 75
    (96,43)  # 80
    ]
class Gun(pygame.sprite.Sprite):
    images = []
    images_loaded = False

    def __init__(self, screen, initialpos):
        pygame.sprite.Sprite.__init__(self)
        # Load all iamges
        if not Gun.images_loaded:
            for str in gimages:
                Gun.images.append(pygame.image.load(str).convert_alpha(screen))
            self.num_gimages = len(gimages)
            Gun.images_loaded = True
        # Initialisation
        self.image = Gun.images[16]
        self.rect = self.image.get_rect()
        self.rect.topleft = initialpos
        (self.ix, self.iy) = initialpos
        self.launchpos = launchpos[0]

    def update(self, mousepos):
        (x,y)=mousepos
        op = float(x - SWIDTH/2)
        adj = float(self.iy -y)
        if (adj<=0):
            return
        angle=math.atan(op / adj)
        angle=math.degrees(angle)
        angle=int(angle/5)
        if angle < -16: 
            angle = -16
        if angle > 16: 
            angle = 16

        self.image = Gun.images[angle+16]
        if angle>=0:
            self.launchpos = launchpos[angle]
        else:
            (x,y)=launchpos[angle*-1]
            self.launchpos = (100-x, y)

