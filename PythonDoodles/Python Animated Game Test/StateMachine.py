import pygame
import time

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

bg = pygame.image.load('background.png')
sbg = pygame.transform.scale(bg,(width,height))

def displayLabels(screen,texts,selected,startLoc = 320):
    labels = []
    selectedColor = (0,255,0)
    otherColor = (255,0,0)
    
    for a in range(0,len(texts)):
        if(a==selected):
            label = myfont.render(options[a], 10,selectedColor,(255,255,255))
        else:
            label = myfont.render(options[a], 10,otherColor,(0,0,0))
        screen.blit(label, (350,(a*100)+startLoc))     
while running:
    time.sleep(0.01)
    screen.blit(sbg,(0,0))
    if state == 0:
        options = ["Start","Instructions","Quit"]
        displayLabels(screen,options,selected)
        if pygame.key.get_pressed()[pygame.K_UP] != 0:
            if(selected > 0):
                selected -= 1
            else:
                selected = len(options)-1
            time.sleep(0.02)
        elif pygame.key.get_pressed()[pygame.K_DOWN] != 0:
            if(selected == len(options)-1):
                selected = 0
            else:
                selected += 1
            time.sleep(0.02)
        elif pygame.key.get_pressed()[pygame.K_RETURN] != 0 and selected == 0:
            state = 1
        elif pygame.key.get_pressed()[pygame.K_RETURN] != 0 and selected == 1:
            state = 2
            selected = 0
            time.sleep(0.02)
        elif pygame.key.get_pressed()[pygame.K_RETURN] != 0 and selected == 2:
            running = False
            break;
        
    elif state == 1:
        execfile("GameMain.py")
        state = 3
        running = True
    elif state == 2:
        options = ["Start","Quit"]
        instr1 = "Use Arrow Keys to Move"
        instr2 = "Press Space to Attack"
        instr3 = "Survive"
        lbl1 = myfont.render(instr1,10,(0,255,255),(255,255,255))
        lbl2 = myfont.render(instr2,10,(0,255,255),(255,255,255))
        lbl3 = myfont.render(instr3,10,(0,255,255),(255,255,255))
        screen.blit(lbl1,(0,0))
        screen.blit(lbl2,(0,75))
        screen.blit(lbl3, (0,150))
        displayLabels(screen,options,selected,500)
        if pygame.key.get_pressed()[pygame.K_UP] != 0:
            if(selected > 0):
                selected -= 1
            else:
                selected = len(options)-1
            time.sleep(0.02)
        elif pygame.key.get_pressed()[pygame.K_DOWN] != 0:
            if(selected == len(options)-1):
                selected = 0
            else:
                selected += 1
            time.sleep(0.02)
        elif pygame.key.get_pressed()[pygame.K_RETURN] != 0 and selected == 0:
            state = 1
        elif pygame.key.get_pressed()[pygame.K_RETURN] != 0 and selected == 1:
            running = False
            break;
    elif state == 3:
        options = ["Replay","Quit"]
        displayLabels(screen,options,selected,500)
        stri = "Game Ogre"
        stri2 = "You survived "+ str(start) +" seconds"
        lbl1 = myfont.render(stri,10,(0,255,0),(255,255,255))
        lbl2 = myfont.render(stri2,10,(0,255,0),(255,255,255))
        screen.blit(lbl1,(0,0))
        screen.blit(lbl2,(0,75))
        if pygame.key.get_pressed()[pygame.K_UP] != 0:
            if(selected > 0):
                selected -= 1
            else:
                selected = len(options)-1
            time.sleep(0.02)
        elif pygame.key.get_pressed()[pygame.K_DOWN] != 0:
            if(selected == len(options)-1):
                selected = 0
            else:
                selected += 1
            time.sleep(0.02)
        elif pygame.key.get_pressed()[pygame.K_RETURN] != 0 and selected == 0:
            state = 1
        elif pygame.key.get_pressed()[pygame.K_RETURN] != 0 and selected == 1:
            running = False
            break;
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
pygame.display.quit()

