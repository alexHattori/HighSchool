from Being import Being

import Constants
class Enemy(Being):
    def __init__(self,x,y,health,screen,target):
        super(Enemy,self).__init__(x,y,health,screen)
        self.target = target
    def update(self):
        if(self.x>self.target.x and abs(self.x-self.target.x)<300):
            self.x-=1
            self.moving = True
            self.right = False
            if(self.leftOb):
                self.jumping = True
            else:
                self.jumping = False
        elif(self.x<self.target.x and abs(self.x-self.target.x)<300):
            self.x+=1
            self.moving = True
            self.right = True
            if(self.rightOb):
                self.jumping = True
            else:
                self.jumping = False
        if not self.jumping:
            self.falling = True
        super(Enemy,self).update()
    def interact(self,otherEntity):
        super(Enemy,self).interact(otherEntity)

