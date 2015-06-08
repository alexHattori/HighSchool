import pygame
from Entity import Entity
from Player import Player
import Constants

class Laser(Entity):

    def __init__(self,x,y,screen,right):
        super(Laser,self).__init__(x,y,screen)
        self.right = right
        self.length = 30
        self.width = 10
        self.contactRect = pygame.Rect(self.x,self.y,30,10)
    def update(self):
        if(self.x<0):
            self.dead = True
        else:
            if(self.right):
                self.x+=Constants.laserSpeed
            else:
                self.x-=Constants.laserSpeed
        self.contactRect = pygame.Rect(self.x,self.y,30,10)
    def interact(self,otherEntity):
        if isinstance(otherEntity,Player):
            otherEntity.health-=Constants.laserDamage
            self.dead = True
    def display(self):
        pygame.draw.rect(self.screen,(0,255,255),self.contactRect,1)
