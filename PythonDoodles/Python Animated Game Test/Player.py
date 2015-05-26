import pygame
from Being import Being
import SpriteSheet

class Player(Being):
    def __init__(self,x,y,health,screen):
        super(Player,self).__init__(x,y,health,screen)
        self.contactRect = pygame.Rect(x+15,y,60,130)
        self.idles = SpriteSheet.SpriteStripAnim('sonicSprites.png',(0,0,95,125),6,-1,True)
        self.runs = SpriteSheet.SpriteStripAnim('sonicSprites.png',(0,250,100,125),9,-1,True)
        self.jumps = SpriteSheet.SpriteStripAnim('sonicSprites.png',(0,450,95,125),5,-1,True)
        self.width = 95
        self.length = 125
    def update(self):
        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
            self.moving = True
            self.right = True
        elif pygame.key.get_pressed()[pygame.K_LEFT] != 0 and self.x>=0:
            self.moving = True
            self.right = False
        else:
            self.moving = False
        if pygame.key.get_pressed()[pygame.K_UP] != 0 and not self.falling:
            self.jumping = True
        super(Player,self).update()
        self.contactRect = pygame.Rect(self.x+15,self.y,60,130)
        if not self.jumping:
            self.falling = True
    def display(self):
        if(self.right):
            if(self.idling):
                self.screen.blit(self.idles.next(),(self.x,self.y))      
            elif(self.moving and not self.jumping):
                self.screen.blit(self.runs.next(),(self.x,self.y))
            elif(self.jumping):
                self.screen.blit(self.jumps.next(),(self.x,self.y))
        else:
            if(self.idling):
                self.screen.blit(pygame.transform.flip(self.idles.next(),True,False),(self.x,self.y))      
            elif(self.moving and not self.jumping):
                self.screen.blit(pygame.transform.flip(self.runs.next(),True,False),(self.x,self.y))
            elif(self.jumping):
                self.screen.blit(pygame.transform.flip(self.jumps.next(),True,False),(self.x,self.y))
