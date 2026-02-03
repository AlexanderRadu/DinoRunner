import random
from .assets_loader import BG, CLOUD
from .config import SCREEN_WIDTH, SCREEN_HEIGHT

class Base:
    def __init__(self):
        self.image = BG
        self.width = self.image.get_width()
        self.x1 = 0
        self.x2 = self.width
        self.y = SCREEN_HEIGHT - self.image.get_height() - 20

    def update(self, velocity):
        self.x1 -= velocity
        self.x2 -= velocity

        if self.x1 <= -self.width:
            self.x1 = self.x2 + self.width
        if self.x2 <= -self.width:
            self.x2 = self.x1 + self.width

    def draw(self, screen):
        screen.blit(self.image, (self.x1, self.y))
        screen.blit(self.image, (self.x2, self.y))

class Cloud:
    start_pos = SCREEN_WIDTH
    stop_pos = SCREEN_WIDTH + 550
    distance = 50

    def __init__(self):
        self.image = CLOUD
        self.x = self.generate_new_x()
        self.y = random.randint(75, 200)

    def generate_new_x(self):
        new_x = random.randint(Cloud.start_pos, Cloud.stop_pos)
        Cloud.stop_pos += Cloud.distance
        Cloud.start_pos += Cloud.distance
        return new_x

    def update(self, game_velocity):
        self.x -= game_velocity // 2
        if self.x <= -self.image.get_width():
            self.x = self.generate_new_x()
            self.y = random.randint(75, 200)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))