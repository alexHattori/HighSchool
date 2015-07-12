import pygame,time,inputbox,sys
from Characters import Invader,Player


## TODO Fix Overlapping Enemies
def strToClass(str):
    return getattr(sys.modules[__name__], str)
class LevelEditor():
    def __init__(self,screen,width,height):
        self.screen = screen
        self.width = width
        self.height = height
        self.bg = pygame.image.load('bg.jpg')
        self.sbg = pygame.transform.scale(self.bg,(self.width,self.height))
        self.bgLoc = (0,0)
        self.entities = []
        p = Player(60,self.entities,screen,width,height)
        self.entities.append(p)
        self.name = ""
        self.types = ['Invader']
        self.keys = [pygame.K_1]
    def saveLevel(self):
        file = open('LevelMap.txt','a')
        text = "\n"+self.name+":"
        for x in self.entities:
            text+= x.__class__.__name__
            text+=('(')
            text+=str(x.x)
            text+=('),')
        text = text[:-1]
        file.write(text)
    def validLoc(self,x,entities):
        for e in entities:
            if not isinstance(e,Player):
                rect = pygame.Rect(e.x,e.y,e.length,e.height)
                newRect = pygame.Rect(x,e.y,e.length,e.height)
                if rect.colliderect(newRect):
                    return False
        return True
    def designLevel(self):
        running = True
        self.name = str(inputbox.ask(self.screen, 'Enter Level Name'))
        while running:
            time.sleep(0.01)
            self.screen.blit(self.sbg,self.bgLoc)
            for a in self.entities:
                a.display()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        running = False
                        self.saveLevel()
                        self.entities = [Player(60,self.entities,self.screen,self.width,self.height)]
                    for i in range(0,len(self.keys)):
                        x = self.keys[i]
                        if event.key == x:                  
                            (mouseX,mouseY) = pygame.mouse.get_pos()
                            if self.validLoc(mouseX,self.entities):
                                self.entities.append(strToClass(self.types[i])(mouseX,self.entities,self.screen,self.width,self.height))
