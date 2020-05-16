#  tutorial 6 - game over text and showing score

import pygame
import time
import random

pygame.font.init()
pygame.init()

font_size = 60
my_font = pygame.font.SysFont("Comic Sans", font_size)

# init variables

win_width, win_height = 1300, 700  # important is only win_height
win = pygame.display.set_mode((win_width, win_height))
win_caption = pygame.display.set_caption("castle_run")

running = True

clock = pygame.time.Clock()

start_FPS = 60
FPS = 60

score = 0
score_text = None


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
        self.running = False
        self.standing = True
        self.dying = False
        self.run_count = 0
        self.roll_count = 0
        self.stand_count = 0
        self.die_count = 0
        self.jump_count = 5.25
        self.current_jump_image = self.jumping_images[0]

    def run(self):
        if self.running:
            if player.run_count + 1 < 4 * len(player.running_images):
                player.run_count += 1
            else:
                player.run_count = 0

            win.blit(self.running_images[self.run_count // 4], (self.x, self.y))

    def roll(self):
        if self.rolling:
            if self.roll_count + 1 < 5 * len(self.rolling_images):
                self.roll_count += 1
            else:
                self.roll_count = 0
                self.rolling = False
                self.running = True

            win.blit(self.rolling_images[self.roll_count // 5], (self.x, self.y))

    def jump(self):
        if self.jumping:
            if self.jump_count >= -5.25:
                self.current_jump_image = self.jumping_images[0]
                neg = 1
                if self.jump_count < 0:
                    self.current_jump_image = self.jumping_images[1]
                    neg = -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 0.25
            else:
                self.jump_count = 5.25
                self.jumping = False
                self.running = True

            win.blit(self.current_jump_image, (self.x, self.y))

    def die(self):
        global score_text
        if self.dying:
            self.y = win_height - self.height - 35
            if self.die_count + 1 < 4 * len(self.dying_images):
                self.die_count += 1
            else:
                self.die_count = 0
                time.sleep(1.5)
                self.dying = False
                self.standing = True

            Layer.show_layer(background_1, background_1.x, background_1.y)
            Layer.show_layer(background_2, background_2.x, background_2.y)
            Layer.show_layer(layer_1, layer_1.x, layer_1.y)
            Layer.show_layer(layer_2, layer_2.x, layer_2.y)
            game_over_button.show_button()
            score_text = my_font.render(f"Your score was: {score}", True, (0, 0, 0))
            win.blit(score_text, (20, 20))
            win.blit(self.dying_images[self.die_count // 4], (self.x, self.y))

    def stand(self):
        global score
        if self.standing:
            score = 0
            if self.stand_count + 1 < 4 * len(self.standing_images):
                self.stand_count += 1
            else:
                self.stand_count = 0

            background_1.x = 0
            background_2.x = background_1.width
            layer_1.x = 0
            layer_2.x = layer_2.width
            Layer.show_layer(background_1, background_1.x, background_1.y)
            Layer.show_layer(layer_1, layer_1.x, layer_1.y)
            win.blit(self.standing_images[self.stand_count // 4], (self.x, self.y))
            start_button.show_button()
            start_button.is_clicked()

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
    def __init__(self, vel):
        self.random_ = random.randint(0, 1)
        self.image = pygame.image.load("obstacle/arrow.png").convert_alpha()
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.x = win_width + self.width  # on the right of the window
        self.y = 600
        #  self.obstacle_list = []
        self.vel = vel
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

    def move_obstacle(self, vel):
        global score
        if self.x > 0 - self.width:
            self.x -= vel
        else:
            self.random_set = False
            self.x = win_width + self.width
            score += 1
            print(score)

        self.show_obstacle()


# Button class
class Button(object):
    def __init__(self, image):
        self.image = image
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.x = win_width // 2 - self.width // 2
        self.y = win_height // 2 - self.height // 2 + 50

    def show_button(self):
        win.blit(self.image, (self.x, self.y))

    def is_clicked(self):
        if self.x < int(pygame.mouse.get_pos()[0]) < self.x + self.width:
            if self.y < int(pygame.mouse.get_pos()[1]) < self.y + self.height:
                if pygame.mouse.get_pressed()[0]:
                    return True


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
arrow_vel = 9
arrow2_move = False
arrow_list = [Obstacle(arrow_vel), Obstacle(arrow_vel)]

# button variable
start_button = Button(pygame.image.load("button/start_button.png").convert_alpha())
game_over_button = Button(pygame.image.load("button/game_over_button.png").convert_alpha())

# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not (player.dying or player.standing):
        Layer.layer_scrolling(background_1, background_2, background_vel)
        Layer.layer_scrolling(layer_1, layer_2, layer_vel)

        score_text = my_font.render(f"Your score: {score}", False, (0, 0, 0))
        win.blit(score_text, (20, 20))

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
        arrow_list[0].move_obstacle(arrow_vel)
        if arrow2_move:
            arrow_list[1].move_obstacle(arrow_vel)

        if score == 5 and 550 < arrow_list[0].x < 600:
            arrow2_move = True

        elif score == 10:
            FPS = 90

        elif 0 < score < 40:
            FPS = start_FPS + score

        #  collision detection for arrows
        for arrow in arrow_list:
            if 200 > arrow.x > 50:
                if arrow.y == 600 and not player.jumping:
                    player.dying = True
                elif arrow.y == 555 and not player.rolling:
                    player.dying = True

    elif player.dying:
        FPS = 60
        player.die()
        player.jumping = False
        player.rolling = False
        player.jump_count = 5.25
        player.roll_count = 0
        arrow2_move = False
        arrow_list[0].x = win_width + arrow_list[0].width
        arrow_list[1].x = win_width + arrow_list[1].width

    elif player.standing:
        player.stand()

    #  button clicking checking
    if start_button.is_clicked():
        player.standing = False
        player.running = True
        player.y = win_height - player.height - 35

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
