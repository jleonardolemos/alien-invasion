from Listeners.base_listener import BaseListener
import pygame
from pubsub import pub

class CheckShipHit(BaseListener):

    def __init__(self, app):
        self.app = app

    def handle(self):
        if pygame.sprite.spritecollideany(self.app.ship, self.app.fleet.aliens):
            pub.sendMessage('ship-hit', app=self.app)

    def build(app):
        listener = CheckShipHit(app)
        listener()