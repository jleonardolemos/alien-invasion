import pygame
from time import sleep
from fleet import Fleet
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from pubsub import pub
from event_map import EventMap

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width,
            self.settings.screen_height
        ))

        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption('Alien Invaders')

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.fleet = Fleet(self)
        self.fleet.create()

        self.play_button = Button(self, "Play")
        EventMap(self)

        self.drawable_components = [
            self.ship,
            self.sb,
            self.fleet
        ]

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.is_active():
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():

            if hasattr(event, 'key'):
                event_name = "event-" + str(event.type) + "." + str(event.key)
            else:
                event_name = "event-" + str(event.type)

            pub.sendMessage(
                event_name,
                event=event,
                app = self
            );

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        
        for drawable in self.drawable_components:
            drawable.draw(self.screen)

        if not self.stats.is_active():
            self.play_button.draw_button()

        pygame.display.flip()

    def _update_bullets(self):
        self.ship.bullets.update()
        self._check_bullet_alien_collisions()

        for bullet in self.ship.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.ship.bullets.remove(bullet)

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.ship.bullets, self.fleet.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.fleet.aliens:
            self.ship.bullets.empty()
            self.fleet.create()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        self.fleet.check_fleet_edges()
        self.fleet.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.fleet.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.fleet.aliens.empty()
            self.ship.bullets.empty()
            self.fleet.create()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.inactive()
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.fleet.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
