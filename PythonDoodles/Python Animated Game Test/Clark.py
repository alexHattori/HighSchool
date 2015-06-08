import pygame
from Enemy import Enemy
from Player import Player
import Laser
import Constants
import SpriteSheet

class Clark(Enemy):
    def __init__(self,x,y,health,screen,target):
        super(Clark,self).__init__(x,y,health,screen,target)
        self.contactRect = pygame.Rect(self.x,self.y,90,130)

        self.width = 60
        self.length = 120

        self.speed = int(self.speed/8)
        self.attacking = False
        self.damage = 0

        self.partner = None
    def update(self):
        self.moving = False
        self.attacking = False
        if(abs(self.x-self.target.x)>50):
            if(self.x>self.target.x):
                self.moving = True
                self.right = False
            elif(self.x<self.target.x):
                self.moving = True
                self.right = True
        else:
            if(self.partner == None):
                self.partner = Laser(self.x+30,self.y+10,self.screen,self.right)
        if(self.partner!=None):
            if(self.partner.dead):
                self.partner = None
        super(Shrek,self).update()
        
        if not self.jumping and not self.bottomOb:
            self.falling = True
        self.contactRect = pygame.Rect(self.x,self.y,90,130)
