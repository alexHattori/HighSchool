import pygame
import random
import math
import time
import Constants

import Barrier
import Player
import Shrek


(width, height) = (1000, 700)
screen = pygame.display.set_mode((width, height))
running = True
pygame.init()

myfont = pygame.font.SysFont("monospace", 72)

pygame.mixer.music.load('bgm.wav')
pygame.mixer.music.play(-1)

entities = []
tiles = []

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
def generateEnemies(start,finish,screen,player):
    numShreks = random.randint(1,3)
    for i in range(0,numShreks):
        x = random.randint(start,finish)
        y = 0
        s = Shrek.Shrek(x,y,95,screen,player)
        entities.append(s)
def onScreen(e):
    return e.rightBound>=0 and e.leftBound<=width and e.bottomBound>=0 and e.topBound<=height
def shiftWorld(os):
    for a in tiles:
        a.x-=os
    for a in entities:
        a.x-=os
player = Player.Player(0,0,95,screen)
entities.append(player)

bar = Barrier.Barrier(0,600,100,100,screen)
tiles.append(bar)
generateTerrain(100,1000)
generateEnemies(100,1000,screen,player)
curVal = 1000
start = time.time()
t = 0
while running:
    screen.blit(sbg,bgLoc)
    if(not player.dead):
        t = time.time()-start
    label = myfont.render(str(t), 10,(255,0,0))
    screen.blit(label,(350,0))
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
        generateEnemies(curVal,curVal+350,screen,player)
        curVal+=200
    if len(entities) == 1:
        generateEnemies(0,700,screen,player)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
##            pygame.display.quit()
            pygame.mixer.music.stop()
        if event.type == pygame.MOUSEBUTTONUP:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            s = Shrek.Shrek(mouseX,mouseY,100,screen,player)
            entities.append(s)
