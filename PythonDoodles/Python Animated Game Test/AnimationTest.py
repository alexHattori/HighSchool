import pygame
import SpriteSheet
import time
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
running = True
pygame.init()
##images = SpriteSheet.SpriteStripAnim('shrek.png',(290,60,40,60),3,-1,True)
##images = SpriteSheet.SpriteStripAnim('shrek.png',(0,73,45,50),6,-1,True)
##images = SpriteSheet.SpriteStripAnim('shrek.png',(5,440,50,50),6,-1,True)
images = SpriteSheet.SpriteStripAnim('sonicSprites.png',(0,380,70,70),4,-1,True)

while running:
    img = pygame.transform.scale(images.next(),(90,130))
    time.sleep(0.1)
    screen.fill((255,255,255))
    screen.blit(img,(300,300))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
