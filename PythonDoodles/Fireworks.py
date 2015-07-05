
import pygame,random,time

background_colour = (0,0,0)
(width, height) = (1000, 700)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Happy 4th of July!')
running = True
items = []

class Firework():
    def __init__(self, x, color, time):
        self.x = x
        self.color = color
        self.time = time
        self.exploding = False
        self.y = 700
        self.rect = pygame.Rect(self.x,self.y,5,10)
    def update(self):
        if(self.time == 0):
            self.exploding = True
        self.time-=1
        if(not self.exploding):
            self.y-=2
        else:
            items.remove(self)
            e = Explosion(self.x,self.y,self.color)
            items.append(e)
    def display(self):
        self.rect = pygame.Rect(self.x,self.y,5,10)
        pygame.draw.rect(screen, self.color,self.rect) 


class Explosion():
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.prongs = 5
        self.particles = []
        self.time = 100
##        for x in range(0,self.prongs):
        p1 = Particle(self.x,self.y,self.color,0,2)
        p2 = Particle(self.x,self.y,self.color,2,1)
        p3 = Particle(self.x,self.y,self.color,2,-1)
        p4 = Particle(self.x,self.y,self.color,-2,-1)
        p5 = Particle(self.x,self.y,self.color,-2,1)
        self.particles.append(p1)
        self.particles.append(p2)
        self.particles.append(p3)
        self.particles.append(p4)
        self.particles.append(p5)
    def update(self):
        for a in self.particles:
            a.update()
        self.time -= 1
        if(self.time<=0):
            items.remove(self)
    def display(self):
        for a in self.particles:
            a.display()
class Particle():
    def __init__(self,x,y,color,xd,yd):
        self.x = x
        self.y = y
        self.color = color
        self.xd = xd
        self.yd = yd
    def update(self):
        self.x-=self.xd
        self.y-=self.yd
    def display(self):
        rect = pygame.Rect(self.x,self.y,5,5)
        pygame.draw.rect(screen,self.color,rect)
while running:
    time.sleep(0.01)
    screen.fill((0,0,0))
    for a in items:
        a.update()
        a.display()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
        elif event.type == pygame.MOUSEBUTTONUP:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            randCol = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            f = Firework(mouseX,randCol,random.randint(50,350))
            items.append(f)
