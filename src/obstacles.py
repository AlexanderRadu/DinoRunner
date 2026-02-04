import random

from .assets_loader import BIRD, LARGE_CACTUS, SMALL_CACTUS
from .config import SCREEN_HEIGHT, SCREEN_WIDTH


class Obstacle:
    start_pos = SCREEN_WIDTH
    stop_pos = SCREEN_WIDTH + 250
    distance = 100

    def __init__(self, images, velocity):
        self.images = images
        self.image = self.images[0]
        self.x = self._generate_new_x()
        self.velocity = velocity

    def _generate_new_x(self):
        new_x = random.randint(Obstacle.start_pos, Obstacle.stop_pos)
        Obstacle.start_pos = new_x + Obstacle.distance
        Obstacle.stop_pos = Obstacle.start_pos + Obstacle.distance * 3
        return new_x

    def update(self, velocity):
        self.x -= velocity
        if self.x <= -self.image.get_width():
            self.x = self._generate_new_x()
            self.image = random.choice(self.images)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class SmallCactus(Obstacle):
    def __init__(self, velocity):
        super().__init__(SMALL_CACTUS, velocity)
        self.y = 572 - self.image.get_height()


class LargeCactus(Obstacle):
    def __init__(self, velocity):
        super().__init__(LARGE_CACTUS, velocity)
        self.y = 572 - self.image.get_height()


class Bird(Obstacle):
    def __init__(self, velocity):
        super().__init__(BIRD, velocity)
        self.y = SCREEN_HEIGHT // 4 + random.randint(0, 150)
        self.index = 0

    def draw(self, screen):
        if self.index >= 19:
            self.index = 0
        self.image = self.images[self.index // 10]
        self.index += 1
        screen.blit(self.image, (self.x, self.y))

    def _generate_new_x(self):
        new_x = random.randint(Obstacle.start_pos + 100, Obstacle.stop_pos + 100)
        return new_x

    def update(self, velocity):
        self.x -= velocity
        if self.x <= -self.image.get_width():
            self.x = self._generate_new_x()
            self.y = SCREEN_HEIGHT // 4 + random.randint(0, 150)
