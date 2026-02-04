import pygame

from .assets_loader import DEAD, DINO_START, DUCKING, JUMP_SOUND, JUMPING, RUNNING


class Dinosaur:
    ANIMATION_TIME = 5 * 2
    Y_POS = 485
    Y_POS_DUCK = 520

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING
        self.start_img = DINO_START
        self.dead_img = DEAD

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = 18
        self.image = self.run_img[0]
        self.x = 80
        self.y = self.Y_POS

    def update(self, user_input, user_mouse_input):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 20:
            self.step_index = 0

        is_jumping_input = (
            user_input[pygame.K_UP] or user_input[pygame.K_SPACE] or user_mouse_input[0]
        )
        is_ducking_input = user_input[pygame.K_DOWN]

        if is_jumping_input and not self.dino_jump and not is_ducking_input:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
            JUMP_SOUND.play()
        elif is_ducking_input and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or is_ducking_input):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

        if is_ducking_input and self.dino_jump:
            self.jump_vel -= 2

    def duck(self):
        self.image = self.duck_img[self.step_index // 10]
        self.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 10]
        self.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.y -= self.jump_vel
            self.jump_vel -= 0.8

        if self.y >= self.Y_POS:
            self.dino_jump = False
            self.y = self.Y_POS
            self.jump_vel = 18

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def draw_start(self, screen):
        screen.blit(self.start_img, (self.x, self.y - 8))

    def draw_dead(self, screen):
        if self.dino_duck:
            screen.blit(self.dead_img, (self.x + 25, self.Y_POS))
        else:
            screen.blit(self.dead_img, (self.x, self.y))
