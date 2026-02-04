import pygame


class CollideObject:
    def __init__(self, image, x, y):
        self.rect = pygame.Rect(x, y, image.get_width(), image.get_height())
        self.image = image
        self._mask = None

    @property
    def mask(self):
        if self._mask is None:
            self._mask = pygame.mask.from_surface(self.image.convert_alpha())
        return self._mask


def check_collision(dino, *obstacles):
    dino_rect = pygame.Rect(
        dino.x, dino.y, dino.image.get_width(), dino.image.get_height()
    )

    for obstacle in obstacles:
        if isinstance(obstacle, list):
            for item in obstacle:
                item_rect = pygame.Rect(
                    item.x, item.y, item.image.get_width(), item.image.get_height()
                )

                if dino_rect.colliderect(item_rect):
                    dino_sprite = CollideObject(dino.image, dino.x, dino.y)
                    item_sprite = CollideObject(item.image, item.x, item.y)
                    if pygame.sprite.collide_mask(dino_sprite, item_sprite):
                        return True
        else:
            item_rect = pygame.Rect(
                obstacle.x,
                obstacle.y,
                obstacle.image.get_width(),
                obstacle.image.get_height(),
            )

            if dino_rect.colliderect(item_rect):
                dino_sprite = CollideObject(dino.image, dino.x, dino.y)
                item_sprite = CollideObject(obstacle.image, obstacle.x, obstacle.y)
                if pygame.sprite.collide_mask(dino_sprite, item_sprite):
                    return True

    return False
