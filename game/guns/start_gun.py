import pygame
from bullet import Bullet
from drawable import Drawable
from updateable import Updateable

class StartGun(Drawable, Updateable):

    def __init__(self, app):
        self.bullets = pygame.sprite.Group()
        self.app = app
        self.bullets_allowed = 3

    def draw(self, surface):
        for bullet in self.bullets:
            bullet.draw_bullet(surface)

    def update(self):
        self.bullets.update()

    def fire(self):
        if len(self.bullets) < self.bullets_allowed:

            new_bullet = Bullet(
                self.app.ship.rect.midtop,
                self.app.settings.bullet_width,
                self.app.settings.bullet_height,
                self.app.settings.bullet_image,
                self.app.settings.bullet_speed
            )

            self.bullets.add(new_bullet)

    def clean_bullets(self):
        self.bullets.empty()
