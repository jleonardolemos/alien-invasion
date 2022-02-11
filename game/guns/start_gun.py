import pygame
from bullet import Bullet
from drawable import Drawable
from game.paths.straight_path import StraightPath
from updateable import Updateable

class StartGun(Drawable, Updateable):

    def __init__(self, app):
        self.__bullets = pygame.sprite.Group()
        self.app = app
        self.bullets_allowed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_image = 'images/bullet_yellow.bmp'

    def draw(self, surface):
        for bullet in self.__bullets:
            bullet.draw_bullet(surface)

    def update(self):
        self.__bullets.update()

    def fire(self):
        if len(self.__bullets) < self.bullets_allowed:

            new_bullet = Bullet(
                self.app.ship.rect.midtop,
                self.bullet_width,
                self.bullet_height,
                self.bullet_image,
                StraightPath()
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