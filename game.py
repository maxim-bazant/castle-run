import pygame

pygame.init()

# init variables
win_width, win_height = 800, 600

win = pygame.display.set_mode((win_width, win_height))
win_caption = pygame.display.set_caption("test1")

running = True

clock = pygame.time.Clock()

FPS = 240

# main loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    win.fill((0, 0, 0))
    player.show_me()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
