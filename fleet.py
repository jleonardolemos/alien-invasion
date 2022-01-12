import pygame
from alien import Alien

class Fleet:

    @staticmethod
    def create_alien(app, alien_number, row_number):
        alien = Alien(app)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        return alien

    @staticmethod
    def create(app):
        alien = Alien(app)
        alien_width, alien_height = alien.rect.size
        available_space_x = app.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        ship_height = app.ship.rect.height
        available_space_y = (app.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                app.aliens.add(
                    Fleet.create_alien(app, alien_number, row_number)
                )
