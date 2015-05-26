import pygame

class Barrier(object):
    def __init__(self,x,y,length,width,screen):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        
        self.leftBound = x
        self.rightBound = x+length
        self.topBound = y
        self.bottomBound = y+width
        
        self.screen = screen
        self.tileDimensions = 100

        self.past = False
        
        image = pygame.image.load('tile.png')
        self.image = pygame.transform.scale(image,(100,100))

        self.contactRect = pygame.Rect(self.x,self.y,self.length,self.width)
    def update(self):
        self.leftBound = self.x
        self.rightBound = self.x+self.length
        self.topBound = self.y
        self.bottomBound = self.y+self.width
        self.contactRect = pygame.Rect(self.x,self.y,self.length,self.width)
        if self.x+self.length<=0:
           self.past = True
    def display(self):
        x = int(self.length/100)
        y = int(self.width/100)
        for i in range(0,x):
            for j in range(0,y):
                self.screen.blit(self.image,(self.x+i*self.tileDimensions,self.y+j*self.tileDimensions))
