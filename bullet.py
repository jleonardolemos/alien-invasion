import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, position, image, path):
        """Create a bullet object at the ship's current position."""
        super().__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.midtop = position
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.path = path

    def update(self):
        self.path.calculate(self)

    def draw_bullet(self, screen):
        screen.blit(self.image, self.rect)