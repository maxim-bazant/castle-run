#  tutorial 2 - background scrolling

import pygame
pygame.init()


class Background(object):
    def __init__(self, image):
        self.x = 0
        self.y = 0
        self.image = image
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height

    def show_and_move_layer(self):
        pass


win_width, win_height = 800, 600
win = pygame.display.set_mode((win_width, win_height))
win_caption = pygame.display.set_caption("test1")

running = True

clock = pygame.time.Clock()

FPS = 30

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
