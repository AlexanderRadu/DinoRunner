import os

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600
TITLE = 'Dino Runner'
FPS = 60

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

MOVEMENT_VELOCITY = 8.5
BG_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)