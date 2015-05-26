import pygame
import random
import math
import time
import Constants

import Barrier
import Player
import Shrek

entities = []
tiles = []

(width, height) = (1000, 700)
screen = pygame.display.set_mode((width, height))
running = True
pygame.init()
pygame.mixer.music.load('bgm.mp3')
pygame.mixer.music.play(-1)

bg = pygame.image.load('background.png')
sbg = pygame.transform.scale(bg,(width,height))
bgLoc = (0,0)

def generateTerrain(start,finish):
    curLen = start
    lastSpace = True
    while curLen < finish:
        leng = random.randint(1,2)
        wid = random.randint(1,3)
        if random.randint(0,5)==1 and not lastSpace:
            if(leng>=2):
                leng = 2
            curLen+= leng*Constants.tileDim
            lastSpace = True
        else:
            lastSpace = False
            barrier = Barrier.Barrier(curLen,height-(wid*Constants.tileDim),leng*Constants.tileDim,wid*Constants.tileDim,screen)
            tiles.append(barrier)
def onScreen(e):
    return e.rightBound>=0 and e.leftBound<=width and e.bottomBound>=0 and e.topBound<=height
def shiftWorld(os):
    for a in tiles:
        a.x-=os
    for a in entities:
        a.x-=os
player = Player.Player(0,0,100,screen)
s = Shrek.Shrek(500,0,100,screen,player)
entities.append(player)
entities.append(s)

bar = Barrier.Barrier(0,600,100,100,screen)
tiles.append(bar)
generateTerrain(100,1000)
curVal = 1000

while running:
    screen.blit(sbg,bgLoc)
    for a in tiles:
        if a.past:
            tiles.remove(a)
            continue;
        if onScreen(a):
            a.display()
            a.update()
    for b in entities:
        if b.dead:
            entities.remove(b)
            continue
        b.update()
        for a in tiles:
            if(b.contactRect.colliderect(a.contactRect)):
                b.interact(a)
        for a in entities:
            if(b.contactRect.colliderect(a.contactRect)):
                b.interact(a)
        if onScreen(b):
            b.display()
    offset = player.x-350
    if offset>=0:
        shiftWorld(offset)
        curVal-=offset
    pygame.display.flip()
    if curVal<=1000:
        generateTerrain(curVal,curVal+350)
        curVal+=200
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
            pygame.mixer.music.stop()
