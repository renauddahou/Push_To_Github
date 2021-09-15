import pygame 
pygame.init()
screen = pygame.display.set_mode((600,600))
done = False
x = 60
y = 60
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.circle(screen, (255,255,255),(300,60), 30)
    pygame.draw.line(screen, (0,255,255),(50,150),(250,150), 10)
    pygame.draw.line(screen, (0,255,255),(150,50),(150,250), 10)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x,y,90,90))
    pygame.display.update()