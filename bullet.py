import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, position, width, height, image, speed):
        """Create a bullet object at the ship's current position."""
        super().__init__()

        self.rect = pygame.Rect(
            0, 0, width, height
        )

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.speed = speed

        self.rect.midtop = position
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self, screen):
        screen.blit(self.image, self.rect)