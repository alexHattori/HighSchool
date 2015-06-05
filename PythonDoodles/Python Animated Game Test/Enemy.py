from Being import Being

import Constants
class Enemy(Being):
    def __init__(self,x,y,health,screen,target):
        super(Enemy,self).__init__(x,y,health,screen)
        self.target = target
    def update(self):
        super(Enemy,self).update()
    def interact(self,otherEntity):
        super(Enemy,self).interact(otherEntity)
    def takeDamage(self,damage):
        self.health-=damage

