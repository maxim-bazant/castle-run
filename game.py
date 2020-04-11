#  tutorial 2 - background scrolling

import pygame
pygame.init()

win_width, win_height = 800, 600
win = pygame.display.set_mode((win_width, win_height))
win_caption = pygame.display.set_caption("test1")

running = True

clock = pygame.time.Clock()

FPS = 30
# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
