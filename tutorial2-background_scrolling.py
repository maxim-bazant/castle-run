import pygame

pygame.init()


class Background:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("images/Background.png")
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height

    def show_background(self):
        win.blit(self.image, (self.x, self.y))

    @staticmethod
    def background_scrolling(bg1, bg2):
        bg1.x += -5
        bg2.x += -5

        bg1.show_background()
        bg2.show_background()

        if bg1.x < -2 * bg1.width + win_width:
            bg1.x = win_width
        if bg2.x < -2 * bg2.width + win_width:
            bg2.x = win_width


# Background() variables
background1 = Background()
background2 = Background()

background2.x = background2.width

# init variables
win_width, win_height = Background().width * 0.33, Background().height

win = pygame.display.set_mode((int(win_width), win_height))
win_caption = pygame.display.set_caption("test1")

running = True

clock = pygame.time.Clock()

FPS = 30

# main loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Background().background_scrolling(background1, background2)
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
quit()
