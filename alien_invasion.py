import pygame
from game.guns.start_gun import StartGun
from fleet import Fleet
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from pubsub import pub
from event_map import EventMap

class AlienInvasion:

    def __init__(self, game_state, settings, screen):
        pygame.init()
        self.settings = settings
        self.game_state = game_state

        self.screen = screen

        pygame.display.set_caption('Alien Invaders')

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.fleet = Fleet(self)
        self.gun = StartGun(self);
        self.fleet.create()

        self.play_button = Button(self, "Play")
        EventMap(self)

        self.drawable_components = {
            "ship": self.ship,
            "sb": self.sb,
            "fleet": self.fleet,
            "play_button": self.play_button,
            "gun": self.gun,
        }

        self.updateable_components = {
            "ship": self.ship,
            "fleet": self.fleet,
            "gun": self.gun,
        }

    def game_loop(self):
        while self.game_state.is_game_running():
            self._check_events()
            self._update()

            pub.sendMessage(
                'move-completed',
                app = self
            );

            self._draw()

    def _update(self):
        if self.stats.is_active():
            
            for updateable in self.updateable_components.values():
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

        for drawable in self.drawable_components.values():
            drawable.draw(self.screen)

        pygame.display.flip()

    def change_gun(self, gun):
        self.gun = gun
        self.drawable_components["gun"] = self.gun
        self.updateable_components["gun"] = self.gun