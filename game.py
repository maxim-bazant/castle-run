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


class Layer(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("images/layer.png")
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height

    def show_me(self):
        win.blit(self.image, (self.x, self.y))

    @staticmethod
    def layer_scrolling(l_1, l_2):
        l_1.x += -3
        l_2.x += -3

        l_1.show_me()
        l_2.show_me()

        if l_1.x < -2 * l_1.width + win_width:
            l_1.x = win_width
        if l_2.x < -2 * l_1.width + win_width:
            l_2.x = win_width


# layer variables
layer_1 = Layer()
layer_2 = Layer()

layer_2.x = layer_2.width


# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.blit(background, (0, 0))
    Layer.layer_scrolling(layer_1, layer_2)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
