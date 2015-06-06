import pygame


background_color = (0,0,255)
colorInt = 0;
forward = True

(width, height) = (1000, 700)
screen = pygame.display.set_mode((width, height))
running = True
pygame.init()


myfont = pygame.font.SysFont("monospace", 72)
state = 0
selected = 0

running = True
while running:
    screen.fill(background_color)
    if(forward):
        colorInt+=2
    else:
        colorInt-=2
    if(colorInt==254 or colorInt==0):
        forward = not(forward)
    background_color = (10,colorInt,100)
    if state == 0:
        options = ["Start"]
        labels = []
        selectedColor = (0,255,0)
        otherColor = (255,0,0)
        if pygame.key.get_pressed()[pygame.K_UP] != 0:
            if(selected > 0):
                selected -= 1
            else:
                selected = len(options)-1
        elif pygame.key.get_pressed()[pygame.K_DOWN] != 0:
            if(selected == len(options)-1):
                selected = 0
            else:
                selected += 1
        elif pygame.key.get_pressed()[pygame.K_RETURN] != 0:
            state = 1
        for a in range(0,len(options)):
            if(a==selected):
                label = myfont.render(options[a], 10,selectedColor)
            else:
                label = myfont.render(options[a], 10,otherColor)
            screen.blit(label, (400,a*300 + 400))     
    elif state == 1:
##        import GameMain
        execfile('GameMain.py')
        state = 0
        screen = pygame.display.set_mode((width, height))
        pygame.init()
        
    print(state)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
