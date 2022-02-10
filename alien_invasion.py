import pygame
from game.guns.start_gun import StartGun
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
        self.gun = StartGun(self);
        self.fleet.create()

        self.play_button = Button(self, "Play")
        EventMap(self)

        self.drawable_components = [
            self.ship,
            self.sb,
            self.fleet,
            self.play_button,
            self.gun,
        ]

        self.updateable_components = [
            self.ship,
            self.fleet,
            self.gun,
        ]

    def run_game(self):
        while True:
            self._check_events()
            self._update()

            pub.sendMessage(
                'move-completed',
                app = self
            );

            self._draw()

    def _update(self):
        if self.stats.is_active():
            
            for updateable in self.updateable_components:
                updateable.update()

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

    def _draw(self):

        background_image = pygame.image.load(self.settings.bg_image).convert()
        self.screen.blit(background_image, [0, 0])        

        for drawable in self.drawable_components:
            drawable.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
