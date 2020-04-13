#  tutorial 2 - background scrolling

import pygame
pygame.init()

# init variables

win_width, win_height = 1100, 500
win = pygame.display.set_mode((win_width, win_height))
win_caption = pygame.display.set_caption("castle_run")

running = True

clock = pygame.time.Clock()

FPS = 30


# layer class
class Layer(object):
    def __init__(self, image):
        self.x = 0
        self.y = 0
        self.image = image
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height

    @staticmethod
    def layer_scrolling(l_1, l_2, l_vel):
        l_1.x -= l_vel
        l_2.x -= l_vel

        win.blit(l_1.image, (l_1.x, l_1.y))
        win.blit(l_2.image, (l_2.x, l_2.y))

        if l_1.x < -2 * l_1.width + win_width:
            l_1.x = win_width
        if l_2.x < -2 * l_2.width + win_width:
            l_2.x = win_width


# layer variables
layer_1 = Layer(pygame.image.load("images/layer.png"))
layer_2 = Layer(pygame.image.load("images/layer.png"))

layer_vel = 5
layer_2.x = layer_2.width
# background variables
background_1 = Layer(pygame.image.load("images/background.png").convert())
background_2 = Layer(pygame.image.load("images/background.png").convert())

background_vel = 0.5
background_2.x = background_2.width


# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Layer.layer_scrolling(background_1, background_2, background_vel)
    Layer.layer_scrolling(layer_1, layer_2, layer_vel)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
