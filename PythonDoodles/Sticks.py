import pygame,random,time,math


background_color = (0,0,0)
(width, height) = (1000,600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sticks')
running = True

hands = []

class Hand():
    def __init__(self,xCoord,color,player):
        self.value = 4
        self.out = False
        self.x = xCoord
        self.color = color
        self.player = player
        if(player):
            self.contactRect = pygame.Rect(xCoord,500,400,500)
    def update(self):
        if(self.value>=5):
            self.out = True
    def display(self):
        (mouseX,mouseY) = pygame.mouse.get_pos()
        mouseRect = pygame.Rect(mouseX,mouseY,1,1)
        if(mouseRect.colliderect(self.contactRect)):
           pygame.draw.rect(screen,(255,255,255),self.contactRect,1)
        if(self.player):
            for i in range(0,self.value):
                rect = pygame.Rect(self.x+(i*70),500,65,700)
                pygame.draw.ellipse(screen,self.color,rect)

h = Hand(0,(255,0,0),True)
hands.append(h)
while running:
    time.sleep(0.01)
    screen.fill((0,0,0))
    for x in hands:
        if x.out:
            hands.remove(x)
        x.update()
        x.display()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
