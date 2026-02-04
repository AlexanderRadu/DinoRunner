import os

import pygame

from .config import ASSETS_DIR

pygame.init()
pygame.mixer.init()


def load_image(path_parts):
    path = os.path.join(ASSETS_DIR, *path_parts)
    if not os.path.exists(path):
        raise FileNotFoundError(f'Asset not found: {path}')
    return pygame.image.load(path)


RUNNING = [load_image(['Dino', 'DinoRun1.png']), load_image(['Dino', 'DinoRun2.png'])]
JUMPING = load_image(['Dino', 'DinoJump.png'])
DUCKING = [load_image(['Dino', 'DinoDuck1.png']), load_image(['Dino', 'DinoDuck2.png'])]
DEAD = load_image(['Dino', 'DinoDead.png'])
DINO_START = load_image(['Dino', 'DinoStart.png'])

SMALL_CACTUS = [
    load_image(['Cactus', 'SmallCactus1.png']),
    load_image(['Cactus', 'SmallCactus2.png']),
    load_image(['Cactus', 'SmallCactus3.png']),
]
LARGE_CACTUS = [
    load_image(['Cactus', 'LargeCactus1.png']),
    load_image(['Cactus', 'LargeCactus2.png']),
    load_image(['Cactus', 'LargeCactus3.png']),
]
BIRD = [load_image(['Bird', 'Bird1.png']), load_image(['Bird', 'Bird2.png'])]

CLOUD = load_image(['Other', 'Cloud.png'])
BG = load_image(['Other', 'Track.png'])
GAME_OVER = load_image(['Other', 'GameOver.png'])
RESET_BUTTON = load_image(['Other', 'Reset.png'])

try:
    JUMP_SOUND = pygame.mixer.Sound(os.path.join(ASSETS_DIR, 'Music', 'Jump Sound.mp3'))
    DEATH_SOUND = pygame.mixer.Sound(
        os.path.join(ASSETS_DIR, 'Music', 'Death sound.mp3')
    )
    HUNDRED_SOUND = pygame.mixer.Sound(
        os.path.join(ASSETS_DIR, 'Music', 'Hundred riched sound.mp3')
    )
except Exception as e:
    print(f'Warning: Sound loading failed. {e}')

    class DummySound:
        def play(self):
            pass

    JUMP_SOUND = DummySound()
    DEATH_SOUND = DummySound()
    HUNDRED_SOUND = DummySound()

FONT_STYLE = 'comicsansms'
