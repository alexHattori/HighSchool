import pygame
import random
import math
import time

background_colour = (0,0,0)
(width, height) = (1000, 700)
elasticity = 0.6


def makeColors((x,y,z),(a,b,c),particle1,particle2):
        particle1.colour = (((x+a)%255),((y+b)%255), ((z+c)%255))
        particle2.colour = (((x+a)%255),((y+b)%255), ((z+c)%255))

def findParticle(particles, x, y):
    for p in particles:
        if math.hypot(p.x-x, p.y-y) <= p.size:
            return p
    return None
def collide(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.hypot(dx, dy)
    if dist < p1.size + p2.size:
        angle = math.atan2(dy, dx) + 0.5 * math.pi
        x = p1.speedx
        y = p1.speedy
        z = p2.speedx
        a = p2.speedy
        
        p1.speedx = (x * (p1.mass - p2.mass) + 2 * p2.mass * z) / (p1.mass + p2.mass)
        p1.speedy = (y * (p1.mass - p2.mass) + 2 * p2.mass * a) / (p1.mass + p2.mass)
        p2.speedx = (z * (p2.mass - p1.mass) + 2 * p1.mass * x) / (p1.mass + p2.mass)
        p2.speedy = (a * (p2.mass - p1.mass) + 2 * p1.mass * y) / (p1.mass + p2.mass)
        
        makeColors(p1.colour,p2.colour,p1,p2)
        overlap = 0.5*(p1.size + p2.size - dist+1)
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
    def __init__(self, (x, y), size, mass=1):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
        self.thickness = 0
        self.forces = []
        self.accelerationX = 0
        self.accelerationY = 0
        self.speedx = 0
        self.speedy = 0
        self.mass = mass
        self.netForceX = 0
        self.netForceY = 0
        self.isPlanet = False
    def addForce(self,force):
        self.forces.append(force)
    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)
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
        if self.isPlanet == False:
            self.getAcceleration()
            self.getSpeed()
            self.x += self.speedx
            self.y -= self.speedy
        elif self.isPlanet == True:
            self.speedx = 0
            self.speedy = 0
    def bounce(self):
        if self.x > width - self.size:
            self.x = 2*(width - self.size) - self.x
            #self.accelerationX = -self.accelerationX
            #self.accelerationY = -self.accelerationY
            self.speedx*=-elasticity
            self.speedy*=elasticity
        elif self.x < self.size:
            self.x = 2*self.size - self.x
            #self.accelerationX = -self.accelerationX
            #self.accelerationY = -self.accelerationY
            self.speedx*=-elasticity
            self.speedy*=elasticity

        if self.y > height - self.size:
            self.y = 2*(height - self.size) - self.y
            #self.accelerationX = -self.accelerationX
            #self.accelerationY = -self.accelerationY
            self.speedx*=elasticity
            self.speedy*=-elasticity

        elif self.y < self.size:
            self.y = 2*self.size - self.y
            #self.accelerationX = -self.accelerationX
            #self.accelerationY = -self.accelerationY
            self.speedx*=elasticity
            self.speedy*=-elasticity

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fun with Forces!')

number_of_particles = 1
my_particles = []

for n in range(number_of_particles):
    size = random.randint(5, 10)
    density = random.randint(1, 1)
    x = random.randint(size, width-size)
    y = random.randint(size, height-size)
    particle = Particle((x, y), size, density*size**2)
    my_particles.append(particle)
    
size = 40
density = random.randint(10, 10)
x= random.randint(size, width-size)
y = random.randint(size, height-size)
particle = Particle((x, y), size, density*size**2)
particle.isPlanet = True
my_particles.append(particle)

##gravity = Force(-10.0,math.pi/2)
g = gravForce()
selected_particle = None
running = True
posX = 0
posY = 0
while running:
##    gravity.addToPs()
    time.sleep(0.01)
    g.experienceG()
    if selected_particle and selected_particle.isPlanet == False:
        (mouseX, mouseY) = pygame.mouse.get_pos()
        dx = mouseX - posX
        dy = mouseY - posY
        selected_particle.x = posX
        selected_particle.y = posY
    elif selected_particle and selected_particle.isPlanet == True:
        (mouseX, mouseY) = pygame.mouse.get_pos()
        selected_particle.x = mouseX
        selected_particle.y = mouseY
    screen.fill(background_colour)

    for i, particle in enumerate(my_particles):
        if particle != selected_particle:
            particle.bounce()
            particle.move()
            for particle2 in my_particles[i+1:]:
                collide(particle, particle2)
        particle.display()
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
               start = time.time()
               size = random.randint(5, 10)
               density = random.randint(1, 1)
               x = random.randint(size, width-size)
               y = random.randint(size, height-size)
               particle = Particle((x, y), size, density*size**2)
               particle.speedx = random.randint(3, 8)
               particle.speedy = random.randint(3, 8)
               my_particles.append(particle)
               
            
        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_particle and selected_particle.isPlanet == False:
                selected_particle.speedx = 0.01*dx
                selected_particle.speedy = 0.01*-dy
                print(dx,dy)
            elif selected_particle and selected_particle.isPlanet == True:
                selected_particle.speedx = 0
                selected_particle.speedy = 0
##            else:
##                size = (int)((10*(time.time()-start))
##                x = Particle((mouseX,mouseY),size,density*size**2)
##                my_particles.append(x)
                
            selected_particle = None
        #time.sleep(0.01)


  
