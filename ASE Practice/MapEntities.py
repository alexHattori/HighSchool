import pygame,Constants

class Player(object):
    def __init__(self,screen,xLoc,yLoc,battler):
        self.screen = screen
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.battler = battler
        self.battling = False
        self.width = Constants.playerWidth
        self.height = Constants.playerHeight
        self.speed = Constants.playerSpeed
        self.right = False
        self.left = False
        self.up = False
        self.down = True
        self.walking = False
    def display(self):
        self.rect = pygame.Rect(self.xLoc,self.yLoc,self.width,self.height)
        pygame.draw.rect(self.screen.getScreen(),(255,0,0),self.rect)
    def updateKey(self,key):
        if pygame.key.get_pressed()[pygame.K_UP] != 0:
            self.yLoc -= self.speed
            self.right = False
            self.left = False
            self.up = True
            self.down = False
        if pygame.key.get_pressed()[pygame.K_DOWN] != 0:
            self.yLoc += self.speed
            self.right = False
            self.left = False
            self.up = False
            self.down = True
        if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
            self.xLoc -= self.speed
            self.right = False
            self.left = True
            self.up = False
            self.down = False
        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
            self.xLoc += self.speed
            self.right = True
            self.left = False
            self.up = False
            self.down = False
        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0 or pygame.key.get_pressed()[pygame.K_LEFT] != 0 or pygame.key.get_pressed()[pygame.K_DOWN] != 0 or pygame.key.get_pressed()[pygame.K_UP] != 0:
            self.walking = True
        else:
            self.walking = False
        
class Tile(object):
    def __init__(self,screen,xLoc,yLoc):
        self.screen = screen
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.width = Constants.tileWidth
        self.height = Constants.tileHeight
        self.rect = pygame.Rect(self.xLoc,self.yLoc,self.width,self.height)
    def display(self):
        self.rect = pygame.Rect(self.xLoc,self.yLoc,self.width,self.height)
        pygame.draw.rect(self.screen.getScreen(),(0,255,0),self.rect)
    def interact(self,player):
        return
class FinalWall(Tile):
    def __init__(self,screen,xLoc,yLoc):
        super(FinalWall,self).__init__(screen,xLoc,yLoc)
    def interact(self,player):
        leftBound = self.xLoc
        rightBound = self.xLoc+self.width
        topBound = self.yLoc
        bottomBound = self.yLoc+self.height
        playerLeft =  player.xLoc
        playerRight = player.xLoc+player.width
        playerTop = player.yLoc
        playerBottom = player.yLoc+player.height
        if(playerTop<=bottomBound and playerBottom>=bottomBound):
            player.yLoc+=1
        elif(playerBottom>=topBound and playerTop<=topBound):
            player.yLoc-=1
        if(playerLeft<=rightBound and playerRight>=rightBound):
            player.xLoc += 1
        elif(playerRight>=leftBound and playerLeft<=leftBound):
            player.xLoc -= 1
    def display(self):
        self.rect = pygame.Rect(self.xLoc,self.yLoc,self.width,self.height)
        pygame.draw.rect(self.screen.getScreen(),(0,0,255),self.rect)
        
