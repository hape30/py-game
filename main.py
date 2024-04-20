import pygame 

pygame.init()
win = pygame.display.set_mode((1600, 1024))
pygame.display.set_caption("Путешествие в Сонном Лесу")

player = pygame.image.load("idle.png")
bg = pygame.image.load("background.jpg")
run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    win.blit(bg, (0, 0 ))
    win.blit(player, (100, 100))
    pygame.display.update()

pygame.quit()