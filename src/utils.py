import pygame

class CollideObject:
    def __init__(self, image, x, y):
        self.rect = pygame.Rect(x, y, image.get_width(), image.get_height())
        self.mask = pygame.mask.from_surface(image.convert_alpha())

def check_collision(dino, *obstacles):
    dino_sprite = CollideObject(dino.image, dino.x, dino.y)

    for obstacle in obstacles:
        if isinstance(obstacle, list):
            for item in obstacle:
                item_sprite = CollideObject(item.image, item.x, item.y)
                if pygame.sprite.collide_mask(dino_sprite, item_sprite):
                    return True
        else:
            item_sprite = CollideObject(obstacle.image, obstacle.x, obstacle.y)
            if pygame.sprite.collide_mask(dino_sprite, item_sprite):
                return True
    return False