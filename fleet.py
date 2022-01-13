from drawable import Drawable
from alien import Alien
import pygame

class Fleet(Drawable):

    def __init__(self, app):
        self.aliens = pygame.sprite.Group()
        self.app = app
    
    def draw(self, surface):
        self.aliens.draw(surface)

    def check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.app.settings.fleet_drop_speed
        self.app.settings.fleet_direction *= -1

    def create(self):
        alien = Alien(self.app)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.app.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        ship_height = self.app.ship.rect.height
        available_space_y = (self.app.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.aliens.add(
                    Fleet.create_alien(self.app, alien_number, row_number)
                )

    def clean(self):
        self.aliens.empty()

    @staticmethod
    def create_alien(app, alien_number, row_number):
        alien = Alien(app)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        return alien