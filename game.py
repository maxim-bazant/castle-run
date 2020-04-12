#  tutorial 2 - background scrolling

import pygame
pygame.init()

# init variables
background = pygame.image.load("images/background.png")

win_width, win_height = background.get_rect().width, background.get_rect().height
win = pygame.display.set_mode((win_width, win_height))
win_caption = pygame.display.set_caption("castle_run")

running = True

clock = pygame.time.Clock()

FPS = 30
# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.blit(background, (0, 0))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
