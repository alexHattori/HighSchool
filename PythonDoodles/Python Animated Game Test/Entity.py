class Entity(object):
    
    def __init__(self,x,y,screen):
        self.x = x
        self.y = y
        self.dead = False
        self.screen = screen
    def update(self):
        return False
    def interact(self,otherEntity):
        return False
    def display(self):
        return False
    def isDead():
        return self.dead
    def setLoc(x,y):
        self.x = x
        self.y = y
