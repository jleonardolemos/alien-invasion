import pygame
from bullet import Bullet
from drawable import Drawable
from updateable import Updateable

class StartGun(Drawable, Updateable):

    def __init__(self, app):
        self.__bullets = pygame.sprite.Group()
        self.app = app
        self.bullets_allowed = 3

    def draw(self, surface):
        for bullet in self.__bullets:
            bullet.draw_bullet(surface)

    def update(self):
        self.__bullets.update()

    def fire(self):
        if len(self.__bullets) < self.bullets_allowed:

            new_bullet = Bullet(
                self.app.ship.rect.midtop,
                self.app.settings.bullet_width,
                self.app.settings.bullet_height,
                self.app.settings.bullet_image,
                self.app.settings.bullet_speed
            )

            self.__bullets.add(new_bullet)

    def clean_bullets(self):
        self.__bullets.empty()

    def get_bullets(self):
        return self.__bullets

    def get_bullets_copy(self):
        return self.__bullets.copy()

    def remove_bullet(self, bullet):
        return self.__bullets.remove(bullet)