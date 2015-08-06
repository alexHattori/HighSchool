from StateMachine import *
import pygame

(width,height) = (500,500)
screen = pygame.display.set_mode((width, height))
pygame.init()
screenInf = ScreenInfo(screen,width,height)

lis = ['Hello',"ijksdxfasdxjkszdx","hello world","hello my name is Alex","jabba the hutt","hello bubba"]
state = OptionState(screenInf,lis,10,100,200,490)

running = True
while(running):
    screen.fill((255,255,255))
    state.display()
    pygame.display.flip()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
        if event.type == pygame.KEYUP:
            state.updateKey(event.key)
