#  tutorial 4 - obstacles and collision

import pygame
import time
import random

pygame.init()

# init variables

win_width, win_height = 1300, 700  # important is only win_height
win = pygame.display.set_mode((win_width, win_height))
win_caption = pygame.display.set_caption("castle_run")

running = True

clock = pygame.time.Clock()

FPS = 50

score = 0


# player class
class Player(object):
    def __init__(self):
        self.running_images = list()
        for i in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]:
            self.running_images.append(pygame.transform.scale(
                pygame.image.load(f"character_animation/running/{i}.png"), (300, 150)).convert_alpha())

        self.rolling_images = list()
        for i in ["01", "02", "03", "04", "05", "01", "02", "03", "04", "05", "06", "07", "08", "09"]:
            self.rolling_images.append(pygame.transform.scale(
                pygame.image.load(f"character_animation/rolling/{i}.png"), (300, 150)).convert_alpha())
        #  double rolling = longer rolling

        self.jumping_images = list()
        for i in ["01", "02"]:
            self.jumping_images.append(pygame.transform.scale(
                pygame.image.load(f"character_animation/jumping/{i}.png"), (300, 150)).convert_alpha())

        self.dying_images = list()
        for i in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]:
            self.dying_images.append(pygame.transform.scale(
                pygame.image.load(f"character_animation/dying/{i}.png"), (300, 150)).convert_alpha())

        self.standing_images = list()
        for i in ["01", "02", "03", "04", "05", "06", "07", "08"]:
            self.standing_images.append(pygame.transform.scale(
                pygame.image.load(f"character_animation/standing/{i}.png"), (300, 150)).convert_alpha())

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
        self.jump_count = 6.5
        self.current_jump_image = self.jumping_images[0]

    def run(self):
        if self.running:
            if player.run_count + 1 < 3 * len(player.running_images):
                player.run_count += 1
            else:
                player.run_count = 0

            win.blit(self.running_images[self.run_count // 3], (self.x, self.y))

    def roll(self):
        if self.rolling:
            if self.roll_count + 1 < 4 * len(self.rolling_images):
                self.roll_count += 1
            else:
                self.roll_count = 0
                self.rolling = False
                self.running = True

            win.blit(self.rolling_images[self.roll_count // 4], (self.x, self.y))

    def jump(self):
        if self.jumping:
            if self.jump_count >= -6.5:
                self.current_jump_image = self.jumping_images[0]
                neg = 1
                if self.jump_count < 0:
                    self.current_jump_image = self.jumping_images[1]
                    neg = -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 0.5
            else:
                self.jump_count = 6.5
                self.jumping = False
                self.running = True

            win.blit(self.current_jump_image, (self.x, self.y))

    def die(self):
        if self.dying:
            self.y = win_height - self.height - 35
            if self.die_count + 1 < 4 * len(self.dying_images):
                self.die_count += 1
            else:
                self.die_count = 0
                time.sleep(1)
                print("show start menu")
                self.dying = False
                self.standing = True

            Layer.show_layer(background_1, background_1.x, background_1.y)
            Layer.show_layer(background_2, background_2.x, background_2.y)
            Layer.show_layer(layer_1, layer_1.x, layer_1.y)
            Layer.show_layer(layer_2, layer_2.x, layer_2.y)
            win.blit(self.dying_images[self.die_count // 4], (self.x, self.y))

    def stand(self):
        if self.standing:
            if self.stand_count + 1 < 4 * len(self.standing_images):
                self.stand_count += 1
            else:
                self.stand_count = 0

            Layer.show_layer(background_1, 0, 0)
            Layer.show_layer(layer_1, 0, 0)
            win.blit(self.standing_images[self.stand_count // 4], (self.x, self.y))

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

    @staticmethod
    def show_layer(layer, layer_x, layer_y):
        win.blit(layer.image, (layer_x, layer_y))

    @staticmethod
    def layer_scrolling(l_1, l_2, l_vel):
        l_1.x -= l_vel
        l_2.x -= l_vel

        Layer.show_layer(l_1, l_1.x, l_1.y)
        Layer.show_layer(l_2, l_2.x, l_2.y)

        if l_1.x < -2 * l_1.width + win_width:
            l_1.x = win_width
        if l_2.x < -2 * l_2.width + win_width:
            l_2.x = win_width


# obstacle class
class Obstacle(object):  # will be spawning by time.set_timer
    def __init__(self):
        self.random_ = random.randint(0, 1)
        self.image = pygame.image.load("obstacle/arrow.png").convert_alpha()
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.x = win_width + self.width  # on the right of the window
        self.y = 600
        #  self.obstacle_list = []
        self.vel = 9
        #  self.show_count = 0
        self.random_set = False
        self.random = 0

    def show_obstacle(self):
        if self.random_set:
            pass
        elif not self.random_set:
            self.random_ = random.randint(0, 1)
            self.random_set = True

        if self.random_ == 0:
            self.y = 600  # spawn down
        elif self.random_ == 1:
            self.y = 555  # spawn up

        win.blit(self.image, (self.x, self.y))

    def move_obstacle(self):
        if self.x > 0 - self.width:
            self.x -= self.vel
        else:
            self.random_set = False
            self.x = win_width + self.width

        self.show_obstacle()


# layer variables
layer_1 = Layer(pygame.image.load("layers/layer.png").convert_alpha())
layer_2 = Layer(pygame.image.load("layers/layer.png").convert_alpha())

layer_vel = 5
layer_2.x = layer_2.width
# background variables
background_1 = Layer(pygame.image.load("layers/background.png").convert())
background_2 = Layer(pygame.image.load("layers/background.png").convert())

background_vel = 2
background_2.x = background_2.width

# player variable
player = Player()

# obstacle variable
arrow = Obstacle()

# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not (player.dying or player.standing):
        Layer.layer_scrolling(background_1, background_2, background_vel)
        Layer.layer_scrolling(layer_1, layer_2, layer_vel)

        keys = pygame.key.get_pressed()

        #  key presses
        if keys[pygame.K_s] and not player.jumping:  # press key s to roll
            player.rolling = True
            player.running = False

        if keys[pygame.K_SPACE] and not player.rolling:  # press space to jump
            player.jumping = True
            player.running = False

        #  character animation
        player.animations_in_action()

        # arrow animation
        arrow.move_obstacle()

        #  collision checking
        if 200 > arrow.x > 50:
            if arrow.y == 600 and not player.jumping:
                player.dying = True
            elif arrow.y == 555 and not player.rolling:
                player.dying = True

    elif player.standing:
        player.stand()

    elif player.dying:
        player.die()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
