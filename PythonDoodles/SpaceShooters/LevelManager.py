import pygame,time
from Characters import Invader,Laser,Player

## TODO    Improve How Characters are Read IE: createCharacters

class LevelManager():
    def __init__(self,screen,width,height):
        self.screen = screen
        self.width = width
        self.height = height
        self.bg = pygame.image.load('bg.jpg')
        self.sbg = pygame.transform.scale(self.bg,(self.width,self.height))
        self.bgLoc = (0,0)
    def winLevel(self,entities):
        for a in entities:
            if(isinstance(a,Invader)):
               return False
        return True

    def gameOver(self,entities):
        for a in entities:
            if(isinstance(a,Player)):
               return False
        return True
    def createCharacter(self,entities,name,loc):
        if(name == 'Invader'):
            a = Invader(int(loc),entities,self.screen,self.width,self.height)
            entities.append(a)
        elif(name == 'Player'):
            a = Player(int(loc),entities,self.screen,self.width,self.height)
            entities.append(a)
    def getEntities(self,name):
        entities = []
        file = open('LevelMap.txt','r')
        textFile = file.read()
        lines = textFile.split('\n')
        for line in lines:
            levelSplit = line.split(':')
            if levelSplit[0] == name:
                chars = levelSplit[1].split(',')
                for x in chars:
                    nameAndLoc = x.split('(')
                    name = nameAndLoc[0]
                    loc = nameAndLoc[1][:-1]
                    self.createCharacter(entities,name,loc)
        return entities
    def runLevel(self,name):
        entities = self.getEntities(name)
        while not(self.gameOver(entities) or self.winLevel(entities)):
            time.sleep(0.01)
            self.screen.blit(self.sbg,self.bgLoc)
            for a in entities:
                if(a.dead):
                    entities.remove(a)
                else:
                    a.update()
                    a.display()
                    a.interact()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    for x in entities:
                        if isinstance(x,Player):
                            entities.remove(x)
        return self.gameOver(entities)
