from Listeners.base_listener import BaseListener
import pygame
from time import sleep
from pubsub import pub

class Die(BaseListener):

    def __init__(self, app):
        self.app = app

    def handle(self):
        if self.app.stats.ships_left > 0:
            self.app.stats.ships_left -= 1
            self.app.sb.prep_ships()
            self.app.fleet.aliens.empty()
            self.app.gun.clean_bullets()
            self.app.fleet.create()
            self.app.ship.center_ship()
            sleep(0.5)
        else:
            pub.sendMessage('game-over', app = self.app)

    def build(app):
        listener = Die(app)
        listener()