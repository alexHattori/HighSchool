import pygame
from Enemy import Enemy
import SpriteSheet

class Shrek(Enemy):
    def __init__(self,x,y,health,screen,target):
        super(Shrek,self).__init__(x,y,health,screen,target)
        self.contactRect = pygame.Rect(self.x,self.y,90,130)
        self.walks = SpriteSheet.SpriteStripAnim('shrek.png',(0,73,45,54),6,-1,True)
        self.attacks = SpriteSheet.SpriteStripAnim('shrek.png',(0,188,45,54),4,-1,True)
        self.jumps = SpriteSheet.SpriteStripAnim('shrek.png',(290,60,40,60),3,-1,True)
    def update(self):
        super(Shrek,self).update()
        self.contactRect = pygame.Rect(self.x,self.y,90,130)
    def display(self):
        img = None
        if(self.right):   
            if(self.moving and not self.jumping):
                img = pygame.transform.scale(self.walks.next(),(90,130))
            elif(self.jumping):
                img = pygame.transform.scale(self.jumps.next(),(90,130))           
        else:
            if(self.moving and not self.jumping):
                img = pygame.transform.scale(self.walks.next(),(90,130))
                img = pygame.transform.flip(img,True,False)
            elif(self.jumping):
                img = pygame.transform.scale(self.jumps.next(),(90,130))
                img = pygame.transform.flip(img,True,False)
        if img != None:
            self.screen.blit(img,(self.x,self.y))
    def interact(self,otherEntity):
        super(Shrek,self).interact(otherEntity)
