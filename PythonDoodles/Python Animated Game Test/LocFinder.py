import pygame

(width, height) = (1000, 700)
screen = pygame.display.set_mode((width, height))
running = True
pygame.init()

img = pygame.image.load('sonicSprites.png')
screen.blit(img,(0,0))
while running:
    screen.blit(img,(0,0))
    pygame.display.flip()
    if pygame.mouse.get_pressed()[2]:
        print(pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
