import pygame
from pygame.sprite import Sprite
from drawable import Drawable
from updateable import Updateable

class Ship(Sprite, Drawable, Updateable):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/green_ship.bmp')
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

    def draw(self, surface):
        surface.blit(self.image, self.rect)