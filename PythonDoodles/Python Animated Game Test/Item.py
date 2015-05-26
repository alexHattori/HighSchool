import Entity

class Item(Entity):
    def __init__(self,x,y,value):
        self.contactRect = pygame.Rect(x,y,10,10)
        self.value = value
        super.__init__(self,x,y)
    def interact(self):
        for a in entities:
            if(isinstance(a,Player)):
                if self.contactRect.collideRect(a.contactRect):
                    self.dead = True
                    return a
