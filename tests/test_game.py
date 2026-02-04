import os
import sys
from unittest.mock import MagicMock, patch

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


mock_pygame = MagicMock()
sys.modules['pygame'] = mock_pygame


class MockSurface:
    def get_width(self):
        return 50

    def get_height(self):
        return 50

    def convert_alpha(self):
        return self


mock_pygame.image.load.return_value = MockSurface()


class MockRect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def colliderect(self, other):
        return (
            self.x < other.x + other.width
            and self.x + self.width > other.x
            and self.y < other.y + other.height
            and self.y + self.height > other.y
        )


mock_pygame.Rect = MockRect

mock_pygame.K_UP = 0
mock_pygame.K_DOWN = 1
mock_pygame.K_SPACE = 2

with patch('os.path.exists', return_value=True):
    from src.config import FPS, SCREEN_WIDTH, TITLE
    from src.dino import Dinosaur
    from src.obstacles import SmallCactus


def test_dino_initialization():
    dino = Dinosaur()
    assert dino.dino_run is True
    assert dino.dino_jump is False
    assert dino.y == Dinosaur.Y_POS


def test_dino_jump_mechanic():
    dino = Dinosaur()
    dino.dino_jump = True
    initial_y = dino.y
    dino.jump()
    assert dino.y < initial_y


def test_dino_duck_state():
    dino = Dinosaur()
    keys = MagicMock()
    keys.__getitem__.side_effect = lambda k: k == mock_pygame.K_DOWN

    dino.update(keys, [False])
    assert dino.dino_duck is True


def test_obstacle_creation():
    cactus = SmallCactus(velocity=20)
    assert cactus.x >= SCREEN_WIDTH

    initial_x = cactus.x
    cactus.update(velocity=10)
    assert cactus.x == initial_x - 10


def test_game_constants():
    assert isinstance(TITLE, str)
    assert FPS > 0
