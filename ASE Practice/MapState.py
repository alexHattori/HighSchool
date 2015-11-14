import pygame,sys,Constants
from StateMachine import *
from MapEntities import *

class MapState(State):
    def __init__(self,screen,player,tiles,lb,rb,tb,bb):
        super(MapState,self).__init__(screen)
        self.player = player
        self.tiles = tiles
        self.leftBound = lb
        self.rightBound = rb
        self.topBound = tb
        self.bottomBound = bb
    def update(self):
        self.player.updateKey(None)
    def display(self):
        for x in self.tiles:
            x.display()
        self.player.display()
    def interact(self):
        for x in self.tiles:
            if x.rect.colliderect(self.player.rect):
                x.interact(self.player)
                
class AtoBatMachine(StateMachine):
    def loopMethods(self):
        super(AtoBatMachine,self).loopMethods()
        if(isinstance(self.currState,MapState)):
           self.currState.interact()

class Map(object):
    class MapRect(object):
        def __init__(self,x,y):
            self.x = x
            self.y = y
            self.width = 1
            self.height = 1
            self.isDone = False
    def __init__(self,screen,url,width,height):
        self.screen = screen
        self.url = url
        self.imgWidth = width
        self.imgHeight = height
        
        self.entities = []
        self.mapImg = pygame.image.load(url)

        self.regTileColor = pygame.Color('RED')
        self.finalTileColor = pygame.Color('BLUE')
    def loadMap(self):
        surf = pygame.Surface((self.imgWidth,self.imgHeight))
        surf.blit(self.mapImg,(0,0))
        
        pa = pygame.PixelArray(surf)
        regularTiles = pa.extract(self.regTileColor)
        finalBlocks = pa.extract(self.finalTileColor)

        ##Shows extracted shape as map is loaded
##        self.screen.getScreen().blit(regularTiles.make_surface(),(0,0))
##        pygame.display.flip()
        
        self.addTiles(regularTiles,Tile)
        self.addTiles(finalBlocks,FinalWall)
        self.borderMap()
        return self.entities
    def addTiles(self,pa,className):
        mapRects = []
        for y in range(0,self.imgHeight):
            x = 0
            while(x<self.imgWidth):
                if(pa[x][y]!=0):
                    xEnd = x
                    while(pa[xEnd][y]!=0):
                        xEnd+=1
                        if(xEnd == self.imgWidth):
                            xEnd -= 1
                            break
                    found = False
                    for m in mapRects:
                        if m.x == x and (m.width == xEnd - x) and not m.isDone:
                            m.height+=1
                            x = xEnd
                            found = True
                            break
                    if not found:
                        nm = self.MapRect(x,y)
                        nm.width = xEnd - x
                        mapRects.append(nm)
                        x = xEnd
                x+=1
            for mr in mapRects:
                if(not mr.isDone):
                    if(mr.y+mr.height<y):
                        mr.isDone = True
        for x in mapRects:
            x.width = (round(float(x.width)/Constants.tileWidth))*Constants.tileWidth
            x.height = (round(float(x.height)/Constants.tileHeight))*Constants.tileHeight
            curY = x.y
            curX = x.x
            while curY<=x.y+x.height:
                while curX<=x.x+x.width:
                    nt = className(self.screen,curX,curY) 
                    curX+=Constants.tileWidth
                    self.entities.append(nt)
                curY+=Constants.tileHeight
                curX = x.x
    def borderMap(self):
        minX = sys.maxint
        maxX = 0
        minY = sys.maxint
        maxY = 0
        for x in self.entities:
            if x.xLoc>=maxX:
                maxX = x.xLoc+x.width
            if x.xLoc<=minX:
                minX = x.xLoc
            if x.yLoc>=maxY:
                maxY = x.yLoc+x.height
            if x.yLoc<=minY:
                minY = x.yLoc
        minX-=Constants.tileWidth
        minY-=Constants.tileHeight
        xLoc = minX
        yLoc = minY
        self.minX = minX
        self.minY = minY
        self.maxX = maxX
        self.maxY = maxY
        while(xLoc<=maxX):
            f = FinalWall(self.screen,xLoc,minY)
            f2 = FinalWall(self.screen,xLoc,maxY)
            self.entities.append(f)
            self.entities.append(f2)
            xLoc+=f.width
        while(yLoc<=maxY):
            f = FinalWall(self.screen,minX,yLoc)
            f2 = FinalWall(self.screen,maxX,yLoc)
            self.entities.append(f)
            self.entities.append(f2)
            yLoc+=f.height
