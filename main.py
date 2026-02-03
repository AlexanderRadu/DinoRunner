import pygame
import sys
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, TITLE, FPS, MOVEMENT_VELOCITY, BG_COLOR, TEXT_COLOR
from src.assets_loader import GAME_OVER, RESET_BUTTON, FONT_STYLE, DEATH_SOUND, HUNDRED_SOUND
from src.dino import Dinosaur
from src.obstacles import SmallCactus, LargeCactus, Bird
from src.environment import Base, Cloud
from src.utils import check_collision

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(FONT_STYLE, 35)

        self.playing = False
        self.running = True
        self.game_speed = MOVEMENT_VELOCITY
        self.score = 0
        self.high_score = 0
        self.death_count = 0

        self.dino = Dinosaur()
        self.base = Base()
        self.clouds = [Cloud() for _ in range(4)]

        self.small_cactus = SmallCactus(self.game_speed)
        self.large_cactus = LargeCactus(self.game_speed)
        self.bird = Bird(self.game_speed)

    def reset_game(self):
        self.game_speed = MOVEMENT_VELOCITY
        self.score = 0
        self.dino = Dinosaur()
        self.small_cactus = SmallCactus(self.game_speed)
        self.large_cactus = LargeCactus(self.game_speed)
        self.bird = Bird(self.game_speed)
        self.base = Base()

    def run(self):
        while self.running:
            if not self.playing:
                if self.death_count == 0:
                    self.show_menu(first_start=True)
                else:
                    self.show_menu(first_start=False)
            else:
                self.play()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                sys.exit()

    def update(self):
        user_input = pygame.key.get_pressed()
        user_mouse_input = pygame.mouse.get_pressed()

        self.dino.update(user_input, user_mouse_input)
        self.base.update(self.game_speed)

        for cloud in self.clouds:
            cloud.update(self.game_speed)

        self.small_cactus.update(self.game_speed)
        self.large_cactus.update(self.game_speed)

        if self.score > 350:
            self.bird.update(self.game_speed)

        self.score += 0.15
        if int(self.score) % 100 == 0 and int(self.score) > 0:
            if int(self.score) % 5 == 0:
                HUNDRED_SOUND.play()

        self.game_speed += 0.002

        obstacles_to_check = [self.small_cactus, self.large_cactus]
        if self.score > 350:
            obstacles_to_check.append(self.bird)

        if check_collision(self.dino, *obstacles_to_check):
            DEATH_SOUND.play()
            pygame.time.delay(500)
            self.playing = False
            self.death_count += 1
            if self.score > self.high_score:
                self.high_score = self.score

    def draw(self):
        self.screen.fill(BG_COLOR)

        for cloud in self.clouds:
            cloud.draw(self.screen)

        self.base.draw(self.screen)
        self.small_cactus.draw(self.screen)
        self.large_cactus.draw(self.screen)

        if self.score > 350:
            self.bird.draw(self.screen)

        self.dino.draw(self.screen)
        self.display_score()

        pygame.display.update()

    def display_score(self):
        score_text = self.font.render(f"Score: {int(self.score)}", True, TEXT_COLOR)
        hs_text = self.font.render(f"HI: {int(self.high_score)}", True, TEXT_COLOR)
        self.screen.blit(score_text, (900, 20))
        self.screen.blit(hs_text, (750, 20))

    def play(self):
        self.reset_game()
        while self.playing:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def show_menu(self, first_start=True):
        self.screen.fill(BG_COLOR)
        self.base.draw(self.screen)

        if first_start:
            self.dino.draw_start(self.screen)
            text = self.font.render("Press any Key to Start", True, TEXT_COLOR)
            self.screen.blit(text, (SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2))
        else:
            self.screen.blit(GAME_OVER, (SCREEN_WIDTH // 2 - 190, SCREEN_HEIGHT // 2 - 50))
            self.screen.blit(RESET_BUTTON, (SCREEN_WIDTH // 2 - 35, SCREEN_HEIGHT // 2 + 30))
            self.dino.draw_dead(self.screen)
            self.display_score()

        pygame.display.update()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    waiting = False
                    sys.exit()
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    self.playing = True
                    waiting = False

if __name__ == "__main__":
    game = Game()
    game.run()