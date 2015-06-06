import pygame
from Enemy import Enemy
from Player import Player
import Constants
import SpriteSheet

class Shrek(Enemy):
    def __init__(self,x,y,health,screen,target):
        super(Shrek,self).__init__(x,y,health,screen,target)
        self.contactRect = pygame.Rect(self.x,self.y,90,130)
        self.idles = SpriteSheet.SpriteStripAnim('shrek.png',(5,440,50,50),6,-1,True)
        self.walks = SpriteSheet.SpriteStripAnim('shrek.png',(0,73,45,50),6,-1,True)
        self.attacks = SpriteSheet.SpriteStripAnim('shrek.png',(0,188,45,54),4,-1,True)
        self.jumps = SpriteSheet.SpriteStripAnim('shrek.png',(290,60,40,60),3,-1,True)
        self.width = 60
        self.length = 120

        self.speed = self.speed/2
        self.attacking = False
        self.damage = 5
    def update(self):
        self.moving = False
        self.attacking = False
        if(abs(self.x-self.target.x)>10):
            if(self.x>self.target.x):
                self.moving = True
                self.right = False
            elif(self.x<self.target.x):
                self.moving = True
                self.right = True
        super(Shrek,self).update()
        if not self.jumping and not self.bottomOb:
            self.falling = True
        self.contactRect = pygame.Rect(self.x,self.y,90,130)
    def display(self):
        img = None
        super(Shrek,self).displayHud()
        if(self.right):   
            if(self.moving and not self.jumping):
                img = pygame.transform.scale(self.walks.next(),(90,130))
            elif(self.jumping):
                img = pygame.transform.scale(self.jumps.next(),(90,130))
            elif(not self.moving):
                img = pygame.transform.scale(self.idles.next(),(90,130))
            if(self.attacking):
                img = pygame.transform.scale(self.attacks.next(),(90,130))
        else:
            if(self.moving and not self.jumping):
                img = pygame.transform.scale(self.walks.next(),(90,130))
                img = pygame.transform.flip(img,True,False)
            elif(self.jumping):
                img = pygame.transform.scale(self.jumps.next(),(90,130))
                img = pygame.transform.flip(img,True,False)
            elif(not self.moving):
                img = pygame.transform.scale(self.idles.next(),(90,130))
                img = pygame.transform.flip(img,True,False)
            if(self.attacking):
                img = pygame.transform.scale(self.attacks.next(),(90,130))
                img = pygame.transform.flip(img,True,False)
        if img != None:
            self.screen.blit(img,(self.x,self.y))
    def interact(self,otherEntity):
        self.bottomOb = False
        if isinstance(otherEntity,Player):
            self.attacking = True
            otherEntity.flinch(self.damage)
            if(self.x>otherEntity.x):
                otherEntity.x-=Constants.flinchDist
            else:
                otherEntity.x+=Constants.flinchDist
        super(Shrek,self).interact(otherEntity)
