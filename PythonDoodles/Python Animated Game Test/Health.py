import Item


class Health(Item):
    def interact(self):
        p = super.interact(self)
        if(isInstance(p,Player)):
            p.health+=self.value
    def display(self):
           pygame.draw.circle
