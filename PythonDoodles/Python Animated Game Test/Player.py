import pygame
from Being import Being
import SpriteSheet
import Constants
from Enemy import Enemy
class Player(Being):
    def __init__(self,x,y,health,screen):
        super(Player,self).__init__(x,y,health,screen)
        self.contactRect = pygame.Rect(x+15,y,60,130)
        self.idles = SpriteSheet.SpriteStripAnim('sonicSprites.png',(0,0,95,125),6,-1,True)
        self.runs = SpriteSheet.SpriteStripAnim('sonicSprites.png',(0,250,100,125),9,-1,True)
        self.jumps = SpriteSheet.SpriteStripAnim('sonicSprites.png',(0,450,95,125),5,-1,True)
        self.attacks = SpriteSheet.SpriteStripAnim('sonicSprites.png',(0,380,70,70),4,-1,True)

        self.width = 95
        self.length = 125
        self.flinching = False
        self.attacking = False
    def update(self):
        self.flinching = False
        self.attacking = False
        self.speed = Constants.speed
        if self.health<self.maxHealth:
            self.health+=1
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
        if pygame.key.get_pressed()[pygame.K_SPACE] != 0:
            if self.right or self.x>0:
                self.attacking = True
                self.moving = True
                self.idling = False
                self.jumping = False
                self.falling = False
                self.speed = Constants.attackSpeed
                self.health-=2
        super(Player,self).update()
        if not self.attacking:
            self.contactRect = pygame.Rect(self.x+15,self.y,60,130)
        else:
            self.contactRect = pygame.Rect(self.x+15,self.y,70,70)
        if not self.jumping:
            self.falling = True
    def flinch(self,damage):
        self.health-=damage
        self.flinching = True
    def display(self):
        super(Player,self).displayHud()
        if(self.right):
            if(self.attacking):
                self.screen.blit(self.attacks.next(),(self.x,self.y))
            elif(self.idling):
                self.screen.blit(self.idles.next(),(self.x,self.y))      
            elif(self.moving and not self.jumping):
                self.screen.blit(self.runs.next(),(self.x,self.y))
            elif(self.jumping):
                self.screen.blit(self.jumps.next(),(self.x,self.y))
            
        else:
            if(self.attacking):
                self.screen.blit(pygame.transform.flip(self.attacks.next(),True,False),(self.x,self.y))
            elif(self.idling):
                self.screen.blit(pygame.transform.flip(self.idles.next(),True,False),(self.x,self.y))      
            elif(self.moving and not self.jumping):
                self.screen.blit(pygame.transform.flip(self.runs.next(),True,False),(self.x,self.y))
            elif(self.jumping):
                self.screen.blit(pygame.transform.flip(self.jumps.next(),True,False),(self.x,self.y))
            
    def interact(self,otherEntity):
        super(Player,self).interact(otherEntity)
        if(isinstance(otherEntity,Enemy) and self.attacking):
            otherEntity.takeDamage(Constants.playerDamage)
