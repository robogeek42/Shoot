import pygame
from pygame.locals import *
from pygame.color import *
import os
import sys
import random
from shoot_globals import *
from thingy import *
from bullet import *
from gun import *

if not pygame.mixer: print 'Warning, sound disabled'

pygame.init()

screen=pygame.display.set_mode(screensize)

pygame.display.set_caption("Shoot The Thingymijob")

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

#grass = pygame.image.load("images/grass_tile_small.jpg").convert()
grassbig =pygame.image.load("images/grass3_big.jpg").convert()
def DrawBackground():
#    img_rect = grass.get_rect()
#    nrows = int(screen.get_height() / img_rect.height) + 1
#    ncols = int(screen.get_width() / img_rect.width) + 1
#
#    for y in range(nrows):
#        for x in range(ncols):
#            img_rect.topleft = (x * img_rect.width,
#                                y * img_rect.height)
#            screen.blit(grass, img_rect)
     screen.blit(grassbig, screen.get_rect())

thingys = pygame.sprite.Group()
num_thingys = 20
for n in range(1, num_thingys):
    x = random.randint(BORDERWIDTH, SWIDTH-BORDERWIDTH-IW)
    y = random.randint(BORDERWIDTH, SHEIGHT-LOWERBORDER-IH)
    thingys.add(Thingy(screen, [x,y]))

bullets = pygame.sprite.Group()

gun = Gun(screen, [SWIDTH/2 - 50, SHEIGHT - 105])

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('sounds', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', fullname
        raise SystemExit, message
    return sound

tank_sound = load_sound("tank.wav")
#grenade_sound = load_sound("grenade.wav")

# This is the main game loop
# --------------------------
# We check for events and react to them in an endless loop
done=False
while done==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        elif ( event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]):
            mouse = pygame.mouse.get_pos()
            (mx,my) = mouse
            if my < SHEIGHT-LOWERBORDER+20:
                (lx,ly) = gun.launchpos
                bullets.add(Bullet(screen, [SWIDTH/2 + lx - 50,SHEIGHT-105+ly],mouse, tank_sound))
                tank_sound.play()

    #screen.fill(THECOLORS["black"])
    DrawBackground()

    collisions = pygame.sprite.groupcollide(bullets, thingys, False, False)
    for bullet, tlist in collisions.iteritems():
        if bullet.current_image < 2:
            bullet.kill()
            bullet.snd.play()
            for t in tlist:
                t.kill()

    thingys.update(pygame.time.get_ticks())
    for t in thingys:
        screen.blit(t.image, t.rect)

    bullets.update(bullets,pygame.time.get_ticks())
    for b in bullets:
        screen.blit(b.image, b.rect)

    gun.update(pygame.mouse.get_pos())
    screen.blit(gun.image, gun.rect)

    # Limit to 20 frames per second
    clock.tick(20)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 

