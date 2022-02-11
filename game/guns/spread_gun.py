import pygame
from bullet import Bullet
from drawable import Drawable
from game.guns.base_gun import BaseGun
from game.paths.straight_path import StraightPath
from updateable import Updateable

class SpreadGun(Drawable, Updateable, BaseGun):

    def __init__(self, app):
        self.__bullets_center = pygame.sprite.Group()
        self.__bullets_left = pygame.sprite.Group()
        self.__bullets_right = pygame.sprite.Group()
        self.app = app
        self.bullets_allowed = 2
        self.bullet_image = 'images/bullet_yellow.bmp'

    def draw(self, surface):
        for bullet in self.__bullets_center:
            bullet.draw_bullet(surface)

        for bullet in self.__bullets_left:
            bullet.draw_bullet(surface)

        for bullet in self.__bullets_right:
            bullet.draw_bullet(surface)

    def update(self):
        self.__bullets_center.update()
        self.__bullets_left.update()
        self.__bullets_right.update()

    def fire(self):
        if len(self.__bullets_center) < self.bullets_allowed:

            new_bullet = Bullet(
                self.app.ship.rect.midtop,
                self.bullet_image,
                StraightPath()
            )

            self.__bullets_center.add(new_bullet)

        if len(self.__bullets_left) < self.bullets_allowed:

            new_bullet = Bullet(
                self.app.ship.rect.midtop,
                self.bullet_image,
                StraightPath(bullet_horizontal_speed=-1)
            )

            self.__bullets_left.add(new_bullet)

        if len(self.__bullets_right) < self.bullets_allowed:

            new_bullet = Bullet(
                self.app.ship.rect.midtop,
                self.bullet_image,
                StraightPath(bullet_horizontal_speed=1)
            )

            self.__bullets_right.add(new_bullet)

    def clean_bullets(self):
        self.__bullets_center.empty()
        self.__bullets_left.empty()
        self.__bullets_right.empty()

    def get_bullets(self):
        return self.__build_bullet_pool()

    def get_bullets_copy(self):
        return self.__build_bullet_pool().copy()

    def remove_bullet(self, bullet):
        self.__bullets_center.remove(bullet)
        self.__bullets_left.remove(bullet)
        self.__bullets_right.remove(bullet)

    def __build_bullet_pool(self):
        bulletPool = pygame.sprite.Group()
        bulletPool.add(self.__bullets_center)
        bulletPool.add(self.__bullets_left)
        bulletPool.add(self.__bullets_right)

        return bulletPool