import pygame,random,math,time


## WHEN ADDING CHARACTERS, APPEND Types and Keys to LevelEditor
## Import to LEVEL Manager

class Invader(object):
    def __init__(self,x,y,entities,screen,screenWidth,screenHeight):
        self.x = x
        self.y = y
        self.dead = False
        self.right = True
        self.speed = 4
        self.length = 30
        self.height = 30
        self.delay = 30
        self.maxDelay = self.delay
        self.rect = pygame.Rect(self.x,self.y,self.length,self.height)
        
        self.entities = entities
        self.screen = screen
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
    def update(self):
        if(self.right):
            self.x+=self.speed
        else:
            self.x-=self.speed
        if(self.x <=0):
            self.right = True
        if(self.x+self.length>=self.screenWidth):
            self.right = False
        if(self.delay<=0):
            self.shoot()
        self.delay-=1
    def shoot(self):
        self.delay = self.maxDelay
        l = Laser(self.x+self.length/2,self.y+self.height,False,self.entities,self.screen,self.screenWidth,self.screenHeight)
        self.entities.append(l)
    def display(self):
        self.rect = pygame.Rect(self.x,self.y,self.length,self.height)
        pygame.draw.rect(self.screen,(255,0,0),self.rect)
    def interact(self):
        for b in self.entities:
            if(b.rect.colliderect(self.rect) and isinstance(b,Invader) and b!= self):
                self.right = not self.right
class DeathRay(Invader):
    def __init__(self,x,y,entities,screen,screenWidth,screenHeight):
        super(DeathRay,self).__init__(x,y,entities,screen,screenWidth,screenHeight)
        self.beam = None
    def update(self):
        if(self.beam):
            if(self.beam.dead):
                self.beam = None
        if(not self.beam):
            super(DeathRay,self).update()
    def shoot(self):
        self.delay = self.maxDelay
        l = Beam(self.x+self.length/2,self.y+self.height,False,self.entities,self.screen,self.screenWidth,self.screenHeight)
        self.entities.append(l)
        self.beam = l
    def display(self):
        self.rect = pygame.Rect(self.x,self.y,self.length,self.height)
        pygame.draw.rect(self.screen,(0,0,255),self.rect)
class Dodger(Invader):
    def __init__(self,x,y,entities,screen,screenWidth,screenHeight):
        super(Dodger,self).__init__(x,y,entities,screen,screenWidth,screenHeight)
    def update(self):
        xMin = self.x
        xMax = self.x+self.length
        move = False
        for x in self.entities:
            if isinstance(x,Laser):
                if x.player and (x.x+x.length>=xMin and x.x<=xMax):
                    self.speed = self.length
                    move = True
        if not move:
            self.speed = 5
        super(Dodger,self).update()
    def display(self):
        self.rect = pygame.Rect(self.x,self.y,self.length,self.height)
        pygame.draw.rect(self.screen,(255,0,255),self.rect)
class Laser(object):
    def __init__(self,x,y,player,entities,screen,screenWidth,screenHeight):
        self.x = x
        self.y = y
        self.player = player
        self.dead = False
        self.speed = 8
        self.length = 5
        self.height = 10
        self.rect = pygame.Rect(self.x,self.y,self.length,self.height)
        if(player):
            self.color = (255,0,255)
        else:
            self.color = (0,255,255)

            
        self.entities = entities
        self.screen = screen
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
    def update(self):
        if(self.player):
            self.y-=self.speed
        else:
            self.y+=self.speed
        if(self.y<0):
            self.dead = True
        if(self.y>self.screenHeight):
            self.dead = True
    def display(self):
        self.rect = pygame.Rect(self.x,self.y,self.length,self.height)
        pygame.draw.rect(self.screen,self.color,self.rect)
    def interact(self):
        for b in self.entities:
            if(isinstance(b,Player)):
                if(b.rect.colliderect(self.rect) and not self.player):
                    b.dead = True
                    self.dead = True
##          Add New Enemies Here  
            elif(isinstance(b,Invader)): ## or isinstance(b,DeathRay)
                if(b.rect.colliderect(self.rect) and self.player):
                    b.dead = True
                    self.dead = True
class Beam(Laser):
    def __init__(self,x,y,player,entities,screen,screenWidth,screenHeight):
        self.x = x
        self.y = y
        self.player = False
        self.dead = False
        self.speed = 8
        self.length = 5
        self.height = 10
        self.rect = pygame.Rect(self.x,self.y,self.length,self.height)
        self.color = (255,255,0)
   
        self.entities = entities
        self.screen = screen
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
    def update(self):
        self.height+=self.speed
        if(self.y+self.height>self.screenHeight):
            self.dead = True
    def display(self):
        self.rect = pygame.Rect(self.x,self.y,self.length,self.height)
        pygame.draw.rect(self.screen,self.color,self.rect)
    def interact(self):
        for b in self.entities:
            if(isinstance(b,Player)):
                if(b.rect.colliderect(self.rect) and not self.player):
                    b.dead = True
                    self.dead = True
##          Add New Enemies Here  
            elif(isinstance(b,Invader)): ## or isinstance(b,DeathRay)
                if(b.rect.colliderect(self.rect) and self.player):
                    b.dead = True
                    self.dead = True
class Player(object):
    def __init__(self,x,y,entities,screen,screenWidth,screenHeight):
        self.length = 30
        self.height = 30
        self.x = x
        self.y = screenHeight - self.height
        self.delay = 15
        self.maxDelay = self.delay
        self.dead = False
        self.speed = 5
        self.rect = pygame.Rect(self.x,self.y,self.length,self.height)

        self.entities = entities
        self.screen = screen
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
    def update(self):
        if(pygame.key.get_pressed()[pygame.K_SPACE] != 0 and self.delay<= 0):
            l = Laser(self.x+self.length/2,self.y,True,self.entities,self.screen,self.screenWidth,self.screenHeight)
            self.entities.append(l)
            self.delay = self.maxDelay
        if(pygame.key.get_pressed()[pygame.K_RIGHT] != 0):
            self.x+=self.speed
        if(pygame.key.get_pressed()[pygame.K_LEFT] != 0):
            self.x-=self.speed
        if(self.x<=0):
            self.x = 0
        if(self.x+self.length>self.screenWidth):
            self.x = self.screenWidth - self.length
        self.delay-=1
    def display(self):
        self.rect = pygame.Rect(self.x,self.y,self.length,self.height)
        pygame.draw.rect(self.screen,(0,255,0),self.rect)
    def interact(self):
        return
