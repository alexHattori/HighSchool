from Entity import Entity
import Barrier
import Constants

class Being(Entity):
    def __init__(self,x,y,health,screen):
        self.health = health
        
        self.moving = False
        self.idling = True
        self.jumping = False
        self.falling = False
        self.right = False
        
        self.leftBound = x
        self.rightBound = x
        self.topBound = y
        self.bottomBound = y

        self.rightOb = False
        self.leftOb = False
        self.bottomOb = False

        self.length = 0
        self.width = 0

        self.jumpTimer = Constants.jumpTimerMax
        super(Being,self).__init__(x,y,screen)
    def update(self):
        if self.moving and self.right:
            self.x+=Constants.speed
        elif self.moving and not self.right:
            self.x-=Constants.speed
        if self.jumping and self.jumpTimer > 0:
            self.y-= int(Constants.gravity*5)
            self.jumpTimer -=1
        elif self.jumping and self.jumpTimer <= 0:
            self.jumping = False
            self.falling = True
            self.jumpTimer = Constants.jumpTimerMax
        if self.falling:
            self.y+=Constants.gravity*5
        self.updateState()
        self.leftBound = self.x
        self.rightBound = self.x + self.width
        self.topBound = self.y
        self.bottomBound = self.y + self.length

        if self.y>Constants.screenHeight:
            self.dead = True
            print('death by falls')
        elif self.health<=0:
            self.dead = True
            print('no health')
    def updateState(self):
        if not self.moving and not self.jumping:
            self.idling = True
        if self.moving or self.jumping:
            self.idling = False
    def interact(self,otherEntity):

        self.rightOb = False
        self.leftOb = False
        self.bottomOb = False
        if isinstance(otherEntity,Barrier.Barrier):
            
            if(self.moving and self.right and self.rightBound>=otherEntity.leftBound and (self.topBound<otherEntity.bottomBound and self.bottomBound>otherEntity.topBound)):
                self.moving = False
                self.updateState()
                self.x = otherEntity.leftBound-self.width
                self.rightOb = True
                print('intersect right')
            elif(self.moving and not self.right and self.leftBound<=otherEntity.rightBound and (self.topBound<otherEntity.bottomBound and self.bottomBound>otherEntity.topBound)):
                self.moving = False
                self.updateState()
                self.x = otherEntity.rightBound
                self.leftOb = True
                print('intersect left')
            elif(self.bottomBound >= otherEntity.topBound and self.bottomBound - otherEntity.topBound < self.length/2.0 and (self.rightBound > otherEntity.leftBound or self.leftBound < otherEntity.rightBound)):
                self.falling = False
                self.y = otherEntity.topBound-self.length
                self.bottomOb = True
