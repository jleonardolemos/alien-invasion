import pygame
from pygame.sprite import Sprite
from bullet import Bullet
from drawable import Drawable

class Ship(Sprite, Drawable):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.__moving_right = False
        self.__moving_left = False
        self.settings = ai_game.settings
        self.x = float(self.rect.x)

    def startMovingRight(self):
        self.__moving_right = True

    def startMovingLeft(self):
        self.__moving_left = True

    def stopMovingRight(self):
        self.__moving_right = False

    def stopMovingLeft(self):
        self.__moving_left = False

    def update(self):
        if self.__moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.__moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    @staticmethod
    def fire(app):
        if len(app.bullets) < app.settings.bullets_allowed:
            new_bullet = Bullet(app)
            app.bullets.add(new_bullet)

    def draw(self, surface):
        surface.blit(self.image, self.rect)