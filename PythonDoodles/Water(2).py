import pygame
import random
import math
import time
from time import sleep


background_colour = (0,0,0)
(width,height) = (1280,700)
elasticity = 0.8

def findParticle(particles, x, y):
    for p in particles:
        if math.hypot(p.x-x, p.y-y) <= p.size:
            return p
    return None
def breakUp(particles):
    (mouseX, mouseY) = pygame.mouse.get_pos()
    for p in particles:
        if math.hypot(p.x-mouseX,p.y-mouseY) <= p.size:
            p.size= (int)(p.size * 0.5)
            size = p.size
            density = 1
            x = p.x
            y = p.y
            particle = Particle((x, y), size, density*size**2)
            my_particles.append(particle)
            sleep(0.01)
def collide(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.hypot(dx, dy)
    x = p1.speedx
    y = p1.speedy
    z = p2.speedx
    a = p2.speedy
    if dist < p1.size + p2.size and p1.colour ==p2.colour:
        if(p1.mass >= p2.mass):
            p1.speedx = (p1.mass*p1.speedx + p2.mass * p2.speedx)/(p1.mass+p2.mass)
            p1.speedy = (p1.mass*p1.speedy + p2.mass * p2.speedy)/(p1.mass+p2.mass)
            p1.mass+=p2.mass
            p1.size = (int)((p1.size**2+p2.size**2)**0.5)
            my_particles.remove(p2)
        else:
            p2.speedx = (p1.mass*p1.speedx + p2.mass * p2.speedx)/(p1.mass+p2.mass)
            p2.speedy = (p1.mass*p1.speedy + p2.mass * p2.speedy)/(p1.mass+p2.mass)
            p2.mass+=p1.mass
            p2.size = (int)((p1.size**2+p2.size**2)**0.5)
            my_particles.remove(p1)
    elif dist < p1.size + p2.size:
        p1.speedx = (x * (p1.mass - p2.mass) + 2 * p2.mass * z) / (p1.mass + p2.mass)
        p1.speedy = (y * (p1.mass - p2.mass) + 2 * p2.mass * a) / (p1.mass + p2.mass)
        p2.speedx = (z * (p2.mass - p1.mass) + 2 * p1.mass * x) / (p1.mass + p2.mass)
        p2.speedy = (a * (p2.mass - p1.mass) + 2 * p1.mass * y) / (p1.mass + p2.mass)
        overlap = 0.5*(p1.size + p2.size - dist+1)
        angle = math.atan2(dy, dx) + 0.5 * math.pi
        p1.x += math.sin(angle)*overlap
        p1.y -= math.cos(angle)*overlap
        p2.x -= math.sin(angle)*overlap
        p2.y += math.cos(angle)*overlap
            
class Force():
    def __init__(self,magnitude,direction):
        self.mag = magnitude
        self.direction = direction
    def addToPs(self):
        for p in my_particles:
            p.addForce(self)
class gravForce():
    def experienceG(self):
        for p in my_particles:
            for q in my_particles:
                if p!=q:
                    r = (((p.x-q.x)**2)+((p.y-q.y)**2))
                    if r>1:
                        wumbo = Force((0.1*(p.mass*q.mass)/r),-math.atan2(p.y-q.y,p.x-q.x))
                        q.addForce(wumbo)
                    else:
                        collide(p,q)

class Particle():
    def __init__(self, (x, y), size, mass):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0,0,255)
        self.thickness = 0
        self.forces = []
        self.accelerationX = 0
        self.accelerationY = 0
        self.speedx = 0
        self.speedy = 0
        self.mass = mass
        self.netForceX = 0
        self.netForceY = 0
        self.isClicked = False
    def addForce(self,force):
        self.forces.append(force)
    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)
        self.drawSpeed()
        self.drawA()
    def getSpeed(self):
        self.speedx+= self.accelerationX
        self.speedy-= self.accelerationY
    def getAcceleration(self):
        self.netForceX = 0
        self.netForceY = 0
        if len(self.forces) > 0:
            for force in self.forces:
                self.netForceX+=math.cos(force.direction)*force.mag
                self.netForceY-=math.sin(force.direction)*force.mag
        self.accelerationX = self.netForceX/self.mass
        self.accelerationY = self.netForceY/self.mass
        del self.forces[:]
    def move(self):
        self.getAcceleration()
        self.getSpeed()
        self.x += self.speedx
        self.y -= self.speedy
    def bounce(self):
        if self.x > width - self.size:
            self.x = 2*(width - self.size) - self.x
            self.speedx *= -elasticity
        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.speedx *= -elasticity
        if self.y > height - self.size:
            self.y = 2*(height - self.size) - self.y
            self.speedy *= -elasticity
        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.speedy *= -elasticity
    def drawSpeed(self):
        xstart = self.x
        ystart = self.y
        xend = (self.x+10*self.speedx)
        yend = (self.y-10*self.speedy)
        start = (xstart,ystart)
        finish = (xend,yend)
        pygame.draw.line(screen, (255,255,255),start ,finish)
    def drawA(self):
        xstart = self.x
        ystart = self.y
        xend = (self.x+100*self.accelerationX)
        yend = (self.y+100*self.accelerationY)
        start = (xstart,ystart)
        finish = (xend,yend)
        pygame.draw.line(screen,(255,0,0),start,finish)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fun with Forces!')

number_of_particles = 1
my_particles = []
my_planets = []

def createGen():
    for n in range(number_of_particles):
        size = random.randint(30, 40)
        density = random.randint(1, 1)
        x = random.randint(size, width-size)
        y = random.randint(size, height-size)
        particle = Particle((x, y), size, density*size**2)
        my_particles.append(particle)
createGen()
##gravity = Force(-10.0,math.pi/2)
g = gravForce()
selected_particle = None
running = True
posX = 0
posY = 0
start = 0
newestP = None
while running:
    g.experienceG()
##    breakUp(my_particles)
    screen.fill(background_colour)
    for i, particle in enumerate(my_particles):
        if particle != newestP:
            particle.bounce()
            particle.move()
            for particle2 in my_particles[i+1:]:
                collide(particle, particle2)
            if particle.size*2 > width or particle.size*2 > height:
                number_of_particles-=1
                my_particles.remove(particle)
        else:
            particle.size += 1
        particle.display()
    if selected_particle:
        (mouseX, mouseY) = pygame.mouse.get_pos()
        dx = mouseX - posX
        dy = mouseY - posY
        selected_particle.x = posX
        selected_particle.y = posY
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            selected_particle = findParticle(my_particles, mouseX, mouseY)
            posX = mouseX
            posY = mouseY
            if selected_particle == None:
               size = 1
               density = 1
               x = mouseX
               y = mouseY
               particle = Particle((x, y), size, density*size**2)
               my_particles.append(particle)
               number_of_particles +=1
               newestP = particle
        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_particle:
                selected_particle.speedx = 0.01*dx
                selected_particle.speedy = 0.01*-dy
            else:
                newestP = None
                
            selected_particle = None


  
