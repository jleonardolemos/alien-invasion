import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, position, width, height, color, speed):
        """Create a bullet object at the ship's current position."""
        super().__init__()

        self.rect = pygame.Rect(
            0, 0, width, height
        )

        self.color = color
        self.speed = speed

        self.rect.midtop = position
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self, screen):
        pygame.draw.rect(
            screen,
            self.color,
            self.rect
        )