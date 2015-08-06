import pygame

class ScreenInfo(object):
    def __init__(self,screen,screenWidth,screenHeight):
        self.screen = screen
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
    def getWidth(self):
        return self.screenWidth
    def getHeight(self):
        return self.screenHeight
    def getScreen(self):
        return self.screen
class State(object):
    def __init__(self,screen):
        self.screen = screen
        self.done = False
    def update(self):
        return
    def display(self):
        return
    def isDone(self):
        return self.done
    def updateKey(self,key):
        return
    def getNextState(self):
        return
class OptionState(State):
    def __init__(self,screen,options,states,fullScreen,x=0,y=0,width = 0,height = 0):
        super(OptionState,self).__init__(screen)
        self.list = options
        self.states = states
        if fullScreen:
            self.x = 0
            self.y = 0
            self.width = screen.getWidth()
            self.height = screen.getHeight()
        else:
            self.x = x
            self.y = y
            self.width = width
            self.height = height
        self.selected = 0
    def display(self):
        labels = []
        startHeight = self.y
        initFontSize = int(self.height/len(self.list)*1.5) # for scaling
        selectedColor = (0,255,0)
        otherColor = (255,0,0)
        curHeight = 0
        for i in range(0,len(self.list)):
            x = self.list[i]
            horizLen = initFontSize*len(x)
            if(horizLen>self.screen.getWidth()):
                fontSize = int(self.width/len(x)*1.5)   #for scaling
            else:
                fontSize = initFontSize
            myfont = pygame.font.SysFont("impact", fontSize)
            if(i == self.selected):
                label = myfont.render(x, 10,selectedColor)
            else:
                label = myfont.render(x, 10,otherColor)
            self.screen.getScreen().blit(label,(self.x,startHeight+curHeight))
            curHeight+=fontSize
    def updateKey(self,key):
        if key == pygame.K_UP:
            self.selected-=1
            if(self.selected < 0):
                self.selected = len(self.list)-1
        if key == pygame.K_DOWN:
            self.selected+=1
            if(self.selected >= len(self.list)):
                self.selected = 0
        if key == pygame.K_RETURN:
            self.done = True
    def getNextState(self):
        return self.states[self.selected]
    
