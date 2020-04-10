import pygame

pygame.init()

width, height = 600, 400
win = pygame.display.set_mode((width, height))
win_caption = pygame.display.set_caption("test1")

running = True

clock = pygame.time.Clock()

FPS = 30

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS)

pygame.quit()
quit()
