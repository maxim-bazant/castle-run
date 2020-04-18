#  tutorial 3 - character animation and movement

import pygame
pygame.init()

# init variables

win_width, win_height = 1300, 700  # important is only win_height
win = pygame.display.set_mode((win_width, win_height))
win_caption = pygame.display.set_caption("castle_run")

running = True

clock = pygame.time.Clock()

FPS = 40

score = 0


# player class
class Player(object):
    def __init__(self):
        #  character images
        self.running_images = [pygame.transform.scale(pygame.image.load("character_animation/running/01.png"), (300, 150)).convert_alpha(),
                               pygame.transform.scale(pygame.image.load("character_animation/running/02.png"), (300, 150)).convert_alpha(),
                               pygame.transform.scale(pygame.image.load("character_animation/running/03.png"), (300, 150)).convert_alpha(),
                               pygame.transform.scale(pygame.image.load("character_animation/running/04.png"), (300, 150)).convert_alpha(),
                               pygame.transform.scale(pygame.image.load("character_animation/running/05.png"), (300, 150)).convert_alpha(),
                               pygame.transform.scale(pygame.image.load("character_animation/running/06.png"), (300, 150)).convert_alpha(),
                               pygame.transform.scale(pygame.image.load("character_animation/running/07.png"), (300, 150)).convert_alpha(),
                               pygame.transform.scale(pygame.image.load("character_animation/running/08.png"), (300, 150)).convert_alpha(),
                               pygame.transform.scale(pygame.image.load("character_animation/running/09.png"), (300, 150)).convert_alpha(),
                               pygame.transform.scale(pygame.image.load("character_animation/running/10.png"), (300, 150)).convert_alpha()]
        self.rolling_images = [pygame.transform.scale(pygame.image.load("character_animation/rolling/01.png"), (300, 150)).convert_alpha(),
                               pygame.transform.scale(pygame.image.load("character_animation/rolling/02.png"), (300, 150)).convert_alpha(),
                               pygame.transform.scale(pygame.image.load("character_animation/rolling/03.png"), (300, 150)).convert_alpha(),
                               pygame.transform.scale(pygame.image.load("character_animation/rolling/04.png"), (300, 150)).convert_alpha(),
                               pygame.transform.scale(pygame.image.load("character_animation/rolling/05.png"), (300, 150)).convert_alpha(),
                               pygame.transform.scale(pygame.image.load("character_animation/rolling/06.png"), (300, 150)).convert_alpha(),
                               pygame.transform.scale(pygame.image.load("character_animation/rolling/07.png"), (300, 150)).convert_alpha(),
                               pygame.transform.scale(pygame.image.load("character_animation/rolling/08.png"), (300, 150)).convert_alpha(),
                               pygame.transform.scale(pygame.image.load("character_animation/rolling/09.png"), (300, 150)).convert_alpha()]
        self.jumping_images = [pygame.transform.scale(pygame.image.load("character_animation/jumping/01.png"), (300, 150)),
                               pygame.transform.scale(pygame.image.load("character_animation/jumping/02.png"), (300, 150)),
                               pygame.transform.scale(pygame.image.load("character_animation/jumping/03.png"), (300, 150))]
        self.dying_images = [pygame.transform.scale(pygame.image.load("character_animation/dying/01.png"), (300, 150)),
                             pygame.transform.scale(pygame.image.load("character_animation/dying/02.png"), (300, 150)),
                             pygame.transform.scale(pygame.image.load("character_animation/dying/03.png"), (300, 150)),
                             pygame.transform.scale(pygame.image.load("character_animation/dying/04.png"), (300, 150)),
                             pygame.transform.scale(pygame.image.load("character_animation/dying/05.png"), (300, 150)),
                             pygame.transform.scale(pygame.image.load("character_animation/dying/06.png"), (300, 150))]
        self.standing_images = [pygame.transform.scale(pygame.image.load("character_animation/standing/01.png"), (300, 150)),
                                pygame.transform.scale(pygame.image.load("character_animation/standing/02.png"), (300, 150)),
                                pygame.transform.scale(pygame.image.load("character_animation/standing/03.png"), (300, 150)),
                                pygame.transform.scale(pygame.image.load("character_animation/standing/04.png"), (300, 150)),
                                pygame.transform.scale(pygame.image.load("character_animation/standing/05.png"), (300, 150)),
                                pygame.transform.scale(pygame.image.load("character_animation/standing/06.png"), (300, 150)),
                                pygame.transform.scale(pygame.image.load("character_animation/standing/07.png"), (300, 150)),
                                pygame.transform.scale(pygame.image.load("character_animation/standing/08.png"), (300, 150))]

        self.width = self.running_images[0].get_rect().width
        self.height = self.running_images[0].get_rect().height
        self.x = 0
        self.y = win_height - self.height - 35
        self.rolling = False
        self.jumping = False
        self.running = True
        self.standing = False
        self.dying = False
        self.run_count = 0
        self.roll_count = 0
        self.stand_count = 0
        self.die_count = 0
        self.jump_count = 0

    def run(self):
        if self.running:
            if player.run_count + 1 < 3 * len(player.running_images):
                player.run_count += 1
            else:
                player.run_count = 0

            win.blit(self.running_images[self.run_count // 3], (self.x, self.y))

    def roll(self):
        if self.rolling:
            if self.roll_count + 1 < 3 * len(self.rolling_images):
                self.roll_count += 1
            else:
                self.roll_count = 0
                self.rolling = False
                self.running = True

            win.blit(self.rolling_images[self.roll_count // 3], (self.x, self.y))

    def jump(self):
        if self.jumping:
            pass  # jump

    def die(self):
        if self.dying:
            if player.die_count + 1 < 3 * len(player.dying_images):
                player.die_count += 1
            else:
                player.die_count = 0

            win.blit(self.dying_images[self.die_count // 3], (self.x, self.y))

    def stand(self):
        if self.standing:
            if player.stand_count + 1 < 3 * len(player.standing_images):
                player.stand_count += 1
            else:
                player.stand_count = 0

            win.blit(self.standing_images[self.stand_count // 3], (self.x, self.y))

    def animations_in_action(self):
        self.roll()
        self.run()
        self.jump()


# layer class
class Layer(object):
    def __init__(self, image):
        self.x = 0
        self.y = 0
        self.image = image
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height

    # I need to create a function that gets the layer to stay in one position for my standing and dying animation

    @staticmethod
    def show_layer(l_1, l_2, l_1_x, l_2_x):   # can delete this because I am going to use win.blit()
        win.blit(l_1.image, (l_1_x, l_1.y))
        win.blit(l_2.image, (l_2_x, l_2.y))

    @staticmethod
    def layer_scrolling(l_1, l_2, l_vel):
        l_1.x -= l_vel
        l_2.x -= l_vel

        Layer.show_layer(l_1, l_2, l_1.x, l_2.x)

        if l_1.x < -2 * l_1.width + win_width:
            l_1.x = win_width
        if l_2.x < -2 * l_2.width + win_width:
            l_2.x = win_width


# layer variables
layer_1 = Layer(pygame.image.load("layers/layer.png").convert_alpha())
layer_2 = Layer(pygame.image.load("layers/layer.png").convert_alpha())

layer_vel = 7
layer_2.x = layer_2.width
# background variables
background_1 = Layer(pygame.image.load("layers/background.png").convert())
background_2 = Layer(pygame.image.load("layers/background.png").convert())

background_vel = 2
background_2.x = background_2.width

# player variables
player = Player()

# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Layer.layer_scrolling(background_1, background_2, background_vel)
    Layer.layer_scrolling(layer_1, layer_2, layer_vel)

    # win.blit(background_1.image, (background_1.x, background_1.y))  # bliting layer 1 and background in one position
    # Layer.show_layer(layer_1, layer_2, layer_1.x, layer_2.x)        # also layer 1 show by bliting
                                                # going to use this when character will be dead or standing

    keys = pygame.key.get_pressed()

    #  key presses
    if keys[pygame.K_s] and not player.jumping:  # press key r to roll
        player.rolling = True
        player.running = False

    #  character animation
    player.animations_in_action()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
