import LevelManager,pygame,time,LevelEditor

background_color = (0,0,0)
(width,height) = (500,500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Shooters')

running = True
pygame.init()

myfont = pygame.font.SysFont("monospace", 72)
myState = 0
option = 0

MENU = 0
LEVEL_SELECT = 1
PLAY = 2
WIN = 3
LOSE = 4
DESIGN_LEVEL = 5
QUIT = 6

lvlMg = LevelManager.LevelManager(screen,width,height)
lvlEd = LevelEditor.LevelEditor(screen,width,height)

curLevel = ""
bg = pygame.image.load('bg.jpg')
sbg = pygame.transform.scale(bg,(width,height))
bgLoc = (0,0)

def displayLabels(screen,texts,selected,start = 0):
    labels = []
    tempH = height-start
    hei = int(tempH/len(texts))
    le = 0
    selectedColor = (0,255,0)
    otherColor = (255,0,0)
    startLoc = (height-hei*len(texts))-start
    for a in range(0,len(texts)):
        if len(texts)<=3:
            fontSize = width/len(options[a])
        else:
            fontSize = (height/len(texts)) - 10
        myfont = pygame.font.SysFont("monospace", fontSize)
        if(a==selected):
            label = myfont.render(options[a], 10,selectedColor,(255,255,255))
        else:
            label = myfont.render(options[a], 10,otherColor,(0,0,0))
        screen.blit(label, (le,(a*hei)+startLoc))    
def getLevelOptions():
    file = open('LevelMap.txt','r')
    text = file.read()
    lines = text.split('\n')
    options = []
    outcomes = []
    for x in lines:
        name = x.split(':')[0]
        options.append(name)
        outcomes.append(PLAY)
    lists = [options,outcomes]
    return lists
while running:
    time.sleep(0.01)

    screen.blit(sbg,bgLoc)
    
    if myState == MENU:
        pygame.display.set_caption('Space Shooters')
        options = ['Start','DesignLevel','Quit']
        outcomes = [LEVEL_SELECT,DESIGN_LEVEL,QUIT]
        if(option>=len(options)):
            option = 0
        displayLabels(screen,options,option)
    if myState == LEVEL_SELECT:
        pygame.display.set_caption('Level Select')
        options = getLevelOptions()[0]
        outcomes = getLevelOptions()[1]
        if(option>=len(options)):
            option = 0
        displayLabels(screen,options,option)
    if myState == PLAY:
        pygame.display.set_caption('Space Shooters')
        val = lvlMg.runLevel(curLevel)
        if val:
            myState = LOSE
        else:
            myState = WIN
    if myState == WIN or myState == LOSE:
        if myState == WIN:
            pygame.display.set_caption('You Win!')
        elif myState == LOSE:
            pygame.display.set_caption('You Lose!')
        options = ['Menu','Quit']
        outcomes = [MENU,QUIT]
        if(option>=len(options)):
            option = 0
        displayLabels(screen,options,option,200)
    if myState == DESIGN_LEVEL:
        lvlEd.designLevel()
        myState = MENU
    if myState == QUIT:
        running = False

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
        if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
            
            if myState == MENU or myState == LEVEL_SELECT or myState == WIN or myState == LOSE:
                myState = outcomes[option]
            if myState == PLAY:
                curLevel = getLevelOptions()[0][option]
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            if myState == MENU or myState == LEVEL_SELECT or myState == WIN or myState == LOSE:
                if(option == len(options)-1):
                    option = 0
                else:
                    option+=1
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            if myState == MENU or myState == LEVEL_SELECT or myState == WIN or myState == LOSE:
                if(option == 0):
                    option = len(options)-1
                else:
                    option-=1
pygame.display.quit()
