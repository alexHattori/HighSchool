import pygame
import random
import math
import time

background_color = (0,0,255)
colorInt = 0;
forward = True

(width, height) = (1000, 700)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Human test')
running = True
pygame.init()
myfont = pygame.font.SysFont("monospace", 72)
state = 0
selected = 0


gravity = 7
offset = 0



class Barrier():
    def __init__ (self,(x,y),leng,wid):
        self.x = x
        self.y = y
        self.leng = leng
        self.wid = wid
        self.rect = pygame.Rect(x,y,leng,wid)
    def update(self):
        for e in enemies:
            if(self.rect.colliderect(e.contactRect)):
                if(e.y+290>self.y and e.x>self.x and e.x<self.x+self.leng):
                    e.y = self.y-290
                if(e.x+120>self.x and e.x-120<self.x and e.y+290 > self.y):
                    e.x = self.x-50
                if(e.x-120<self.x+self.leng and e.x+120 > self.x+self.leng and e.y+290 > self.y):
                    e.x = self.x+self.leng+120
        if(self.rect.colliderect(player.contactRect)):
            if(player.y+290>self.y):
                player.falling = False
                player.walking = True
                player.y-=gravity
            if(player.y+290>self.y and player.x>self.x and player.x<self.x+self.leng):
                player.y = self.y-290
            if(player.x+120>self.x and player.x-120<self.x and player.y+290 > self.y):
                player.x = self.x-120
            if(player.x-120<self.x+self.leng and player.x+120 > self.x+self.leng and player.y+290 > self.y):
                player.x = self.x+self.leng+120
        self.rect = pygame.Rect(self.x,self.y,self.leng,self.wid)
    def display(self):
        pygame.draw.rect(screen,(165,42,42),self.rect,0)
class Space(Barrier):
    def update(self):
        print("")
    def display(self):
        print("")
class Enemy(object):
    def __init__(self,(x,y), health,damage):
        self.x = x
        self.y = y
        self.health = health
        self.damage = damage
        self.dead = False
        self.contactRect = pygame.Rect(x-10,y-10,20,20)
    def update(self):
        if(self.contactRect.colliderect(player.contactRect)):
           player.health-=self.damage
           player.gettingHit = True
           walking = False
           jumping = False
           if(player.y+290<self.y):
                player.y-=50
           if(player.x>self.x):
                player.x+=30
                player.updatePos()
                player.updateStatus()
                player.display()
           else:
                player.x-=30
                player.updatePos()
                player.updateStatus()
                player.display()
           self.health-=self.damage
        if(self.health<=0):
            self.dead = True
            enemies.remove(self)
        self.contactRect = pygame.Rect(self.x-10,self.y-10,20,20)
    def display(self):
        pygame.draw.circle(screen,(255,0,255),(self.x,self.y),10,0)
        pygame.draw.rect(screen,(255,0,0),self.contactRect,1)
class Torbot(Enemy):
    def __init__(self,(x,y),health,damage):
        self.x = x
        self.y = y
        self.health = health
        self.damage = damage
        self.dead = False
        self.rect = pygame.Rect(x-10,y-10,20,20)
        
        self.headColor = (255,255,255)
        self.bodyColor = (255,0,0)
        self.armColor = (0,0,0)
        self.head = ((x-120,y-50),(x+120,y-50),(x+80,y+50),(x-80,y+50))
        self.body = (x-80,y+50,160,200)
        self.arm1start = (self.x-150,self.y+100)
        self.arm1finish = (self.x-80,self.y+100)
        self.arm2start = (self.x+80,self.y+100)
        self.arm2finish = (self.x+150,self.y+100)
        self.leg1start = (self.x-80,self.y+250)
        self.leg1finish = (self.x-80-45,self.y+250+45)
        self.leg2start = (self.x+80,self.y+250)
        self.leg2finish = (self.x+80+45,self.y+250+45)
        self.leye = (x-60,y-30)
        self.reye = (x+60,y-30)
        self.antennaStart = (self.x,self.y-50)
        self.antennaFinish = (self.x+20,self.y-80)
        self.contactRect = pygame.Rect(self.x-120,y-50,240,350)
    def update(self):
        x = self.x
        y = self.y
        self.head = ((x-120,y-50),(x+120,y-50),(x+80,y+50),(x-80,y+50))
        self.body = (x-80,y+50,160,200)
        self.leg1start = (self.x-80,self.y+250)
        self.leg1finish = (self.x-80-45,self.y+250+45)
        self.leg2start = (self.x+80,self.y+250)
        self.leg2finish = (self.x+80+45,self.y+250+45)
        self.arm1start = (self.x-150,self.y+100)
        self.arm1finish = (self.x-80,self.y+100)
        self.arm2start = (self.x+80,self.y+100)
        self.arm2finish = (self.x+150,self.y+100)
        self.leye = (x-60,y-10)
        self.reye = (x+60,y-10)
        self.antennaStart = (self.x,self.y-50)
        self.antennaFinish = (self.x+20,self.y-80)

        self.y+=gravity
        super(Torbot, self).update()
        self.contactRect = pygame.Rect(self.x-120,y-50,240,350)
    def display(self):
         pygame.draw.rect(screen,self.bodyColor,self.body,0)
         pygame.draw.polygon(screen,self.headColor,self.head,0)
         pygame.draw.line(screen,self.armColor,self.leg1start,self.leg1finish,5)
         pygame.draw.line(screen,self.armColor,self.leg2start,self.leg2finish,5)
         pygame.draw.line(screen,self.armColor,self.arm1start,self.arm1finish,5)
         pygame.draw.line(screen,self.armColor,self.arm2start,self.arm2finish,5)
         pygame.draw.circle(screen,self.armColor,self.leye,15,5)
         pygame.draw.circle(screen,self.armColor,self.reye,15,5)
         pygame.draw.circle(screen,self.armColor,self.leye,5,0)
         pygame.draw.circle(screen,self.armColor,self.reye,5,0)
         pygame.draw.line(screen,self.armColor,self.antennaStart,self.antennaFinish,5)
         pygame.draw.circle(screen,self.armColor,self.antennaFinish,10,0)
         
         pygame.draw.rect(screen,self.bodyColor,self.contactRect,1)
class Item():
    def __init__(self,(x,y)):
        self.x = x
        self.y = y
        self.val = 1
    def update(self):
        self.val+=1
    def display():
        pygame.draw.circle(screen,(255,255,255),(self.x,self.y),40,0)
        
class Health(Item)  :
    def __init__(self,(x,y),value):
        self.x = x
        self.y = y
        self.value = value
        self.dead = False
        self.rect = pygame.Rect(x-40,y-40,80,80)
    def update(self):
        if(self.rect.colliderect(player.contactRect)):
           player.health+=self.value
           self.dead = True
        self.rect = pygame.Rect(self.x-40,self.y-40,80,80)
    def display(self):
        pygame.draw.circle(screen,(255,255,255),(self.x,self.y),40,0)
        pygame.draw.rect(screen,(255,0,0),self.rect,1)
class Ammo(Item):
    def __init__(self,(x,y),value):
        self.x = x
        self.y = y
        self.value = value
        self.dead = False
        self.rect = pygame.Rect(x-40,y-40,80,80)
    def update(self):
        if(self.rect.colliderect(player.contactRect)):
           player.ammo+=self.value
           self.dead = True
        self.rect = pygame.Rect(self.x-40,self.y-40,80,80)
    def display(self):
        pygame.draw.circle(screen,(255,0,255),(self.x,self.y),40,0)
        pygame.draw.rect(screen,(255,0,0),self.rect,1)
class Laser(Item):
    def __init__(self,(x,y),(a,b)):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.dead = False
        self.timer = 5
    def update(self):
        self.timer-=1
        if(not self.dead and self.timer ==0):
            self.dead = True
        rect = pygame.Rect(self.a,self.b,1,1)
        for e in enemies:
            if(rect.colliderect(e.contactRect)):
                e.health-=2
    def display(self):
        pygame.draw.line(screen,(255,255,0),(self.x,self.y),(self.a,self.b),5)
class Player():
    def __init__(self, (x,y), health) :
        self.x = x
        self.y = y
        self.health = health
        self.ammo = 5
        self.maxHealth = 100
        self.maxAmmo = 5
        
        self.walking = True
        self.falling = False
        self.jumping = False
        self.gettingHit = False
        self.dead = False
        
        self.contactRect = pygame.Rect(x-120,y-50,240,340)
        self.delay = 0
        self.flinchTimer = 0
        
        self.skinColor = (226,188,122)
        self.bodyColor = (255,0,0)
        self.armColor = (0,255,0)
        self.legColor = (0,0,255)
        self.eyeColor = (255,255,255)
        self.pupilColor = (0,0,0)
        self.noseColor = (255,0,0)
        self.mouthColor = (255,0,0)
        self.hairColor = (0,0,0)
        self.buckleColor = (255,255,0)
        self.shoeColor = (0,0,20)
        
        self.body = (x-50,y+80,100,100)
        self.rSleeve = (x-80,y+50,40,50)
        self.lSleeve = (x+40,y+50,40,50)
        self.rArm1 = (x-120,y+60,40,30)
        self.lArm1 = (x+80,y+60,40,30)
        self.lleg = (x-50,y+180 ,30,100)
        self.rleg = (x+20,y+180,30,100)
        self.leye = (x-20,y-10)
        self.reye = (x+20,y-10)
        self.nose = ((x,y),(x-5,y+10),(x+5,y+10))
        self.mouthRect = (x-20,y+10,40,30)
        self.hairRect = (x-30, y-50, 60,20)
        self.pantRect = (x-50,y+150,100,30)
        self.buckleRect = (x-10,y+160,20,10)
        self.lShoeRect = (x-70,y+270,50,20)
        self.rShoeRect = (x+20,y+270,50,20)
    def update(self):
        self.updatePos()
        self.updateStatus()
    def updatePos(self):
        if(self.walking):
            if(pygame.key.get_pressed()[pygame.K_w] != 0):
                self.y-=5
                self.jumping = True
                self.walking = False
                self.delay = 15
        elif(self.jumping):
            if(self.delay>0):
                self.delay-=1
                self.y-=20
            else:
                self.falling = True
                self.jumping = False
                walking = False
        if(self.gettingHit):
           self.skinColor = (255,0,0)
           self.gettingHit = False
        else:
           self.skinColor = (226,188,122)
        if(pygame.key.get_pressed()[pygame.K_d] != 0):
            self.x+=5
        if(pygame.key.get_pressed()[pygame.K_a] != 0):
            self.x-=5
        if(self.y<50):
            self.y=50
        elif(self.y>700):
            self.dead = True
        self.y+=gravity
        self.contactRect = (self.x-50,self.y-50,100,340)
    def updateStatus(self):
        if(pygame.key.get_pressed()[pygame.K_SPACE] != 0 and self.ammo > 0):
            dist = 501
            nearest = None
            for e in enemies:
                if math.hypot(e.x-self.x,e.y-self.y) <=dist:
                    nearest = e
                    dist = math.hypot(e.x-self.x,e.y-self.y)
            if nearest != None and dist<500:
                self.ammo-=1
                (mouseX, mouseY) = pygame.mouse.get_pos()
                laser = Laser((self.x,self.y),(mouseX,mouseY))
                items.append(laser)
                time.sleep(0.1)
        if(self.health>self.maxHealth):
            self.health = self.maxHealth
        if(self.ammo > self.maxAmmo):
            self.ammo = self.maxAmmo
        if(self.health<=0):
            self.dead = True
    def display(self):
        x = (int(self.x))
        y = (int(self.y))
        self.body = (x-50,y+80,100,100)
        self.rSleeve = (x-80,y+50,40,50)
        self.lSleeve = (x+40,y+50,40,50)
        self.rArm1 = (x-120,y+60,40,30)
        self.lArm1 = (x+80,y+60,40,30)
        self.lleg = (x-50,y+180 ,30,100)
        self.rleg = (x+20,y+180,30,100)
        self.leye = (x-20,y-10)
        self.reye = (x+20,y-10)
        self.nose = ((x,y),(x-5,y+10),(x+5,y+10))
        self.mouthRect = (x-20,y+10,40,30)
        self.hairRect = (x-30, y-50, 60,20)
        self.pantRect = (x-50,y+150,100,30)
        self.buckleRect = (x-10,y+160,20,10)
        self.lShoeRect = (x-70,y+270,50,20)
        self.rShoeRect = (x+20,y+270,50,20)
        pygame.draw.rect(screen,self.bodyColor, self.body, 0)
        pygame.draw.circle(screen,self.bodyColor,(x,y+80),50,0)
        pygame.draw.rect(screen,self.bodyColor,self.rSleeve,0)
        pygame.draw.rect(screen,self.bodyColor,self.lSleeve,0)
        pygame.draw.rect(screen,self.skinColor,self.rArm1,0)
        pygame.draw.rect(screen,self.skinColor,self.lArm1,0)
        pygame.draw.ellipse(screen,self.shoeColor,self.lShoeRect,0)
        pygame.draw.ellipse(screen,self.shoeColor,self.rShoeRect,0)
        pygame.draw.rect(screen,self.legColor,self.lleg,0)
        pygame.draw.rect(screen,self.legColor,self.rleg,0)
        pygame.draw.rect(screen,self.legColor,self.pantRect,0)
        pygame.draw.rect(screen,self.buckleColor,self.buckleRect,2);
        pygame.draw.circle(screen,self.skinColor,(x,y),50,0)
        pygame.draw.circle(screen, self.eyeColor, self.leye,10,0)
        pygame.draw.circle(screen, self.eyeColor, self.reye,10,0)
        pygame.draw.circle(screen, self.pupilColor, self.leye,5,0)
        pygame.draw.circle(screen, self.pupilColor, self.reye,5,0)
        pygame.draw.polygon(screen,self.noseColor,self.nose,0)
        pygame.draw.arc(screen,self.mouthColor,self.mouthRect,3,6.5,2)
        pygame.draw.arc(screen,self.hairColor,self.hairRect,0,3.14,10)
        pygame.draw.rect(screen,(255,0,0),self.contactRect,1)
        
        pygame.draw.rect(screen,(255,255,255),(0,0,150,60),0)
        pygame.draw.rect(screen,(255,255,255),(0,60,150,60),0)
        label = myfont.render(str(self.health), 10, (0,255,0))
        label2 = myfont.render(str(self.ammo), 10, (0,255,0))
        screen.blit(label, (0,0))
        screen.blit(label2, (0,60))
def shiftEntities(stuff,forward):
    for a in stuff:
        if(forward):
            a.x-=int(offset*0.01)
        else:
            a.x+=int(offset*0.01)

def generateTerrain():
    length = 1000
    while length < 100000:
        if(random.randint(0,1)==0):
            curLen = random.randint(100,150)
            length+=curLen
        else:
            curLen = random.randint(50,600)
            curHeight = random.randint(0,200)
            bar = Barrier((length,700-curHeight),curLen,curHeight)
            length+=curLen
            tiles.append(bar)
def resetGame():
    player = Player((130,300), 100)
    enemy = Enemy((500,500), 50,10)
    enemy2 = Enemy((600,600), 50,10)
    health = Health((300,200),10)
    ammo = Ammo((300,100),10)
    barrier = Barrier((0,650),400,50)
    barrier2 = Barrier((400,500),300,200)
    barrier3 = Barrier((700,650),300,50)
    tiles = [barrier,barrier2,barrier3]
    enemies = [enemy,enemy2]
    items = [health,ammo]
    
player = Player((130,300), 100)
enemy = Enemy((500,500), 50,10)
enemy2 = Enemy((600,600), 50,10)
torbot = Torbot((800,200),50,10)
health = Health((300,200),10)
ammo = Ammo((300,100),10)
barrier = Barrier((0,650),400,50)
barrier2 = Barrier((400,500),300,200)
barrier3 = Barrier((700,650),300,50)
tiles = [barrier,barrier2,barrier3]
generateTerrain()
enemies = [torbot]
items = [health,ammo]

while running:
    time.sleep(0.01)
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
    if state == 1:
        offset = abs(player.x - (width/2))
        if(offset>5):
            if(player.x>width/2):
                shiftEntities(tiles,True)
                shiftEntities(enemies,True)
                shiftEntities(items,True)
                player.x-=int(offset*0.01)
            elif(player.x<width/2):
                shiftEntities(tiles,False)
                shiftEntities(enemies,False)
                shiftEntities(items,False)
                player.x+=int(offset*0.01)
        player.update()
        for t in tiles:
            t.update()
            t.display()
        for e in enemies:
            if(not e.dead):
                e.update()
                e.display()
            else:
                remove(e)
        for i in items:
            if(not i.dead):
                i.update()
                i.display()
            else:
                items.remove(i)
        player.display()
        if(player.dead):
            state = 3
    if state == 3:
        screen.fill((255,0,0))
        label = myfont.render('You dun goofed', 10, (0,255,255))
        screen.blit(label, (200,300))
##        label2 = myfont.render('Retry?' , 10, (0,255,0))
##        screen.blit(label2,(300,500))
##        if pygame.key.get_pressed()[pygame.K_RETURN] != 0:
##            print('Reset')
##            state = 0
##            running = True
##            resetGame()
##            player.dead = False
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
pygame.display.quit()
