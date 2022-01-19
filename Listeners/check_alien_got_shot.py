from Listeners.base_listener import BaseListener
import pygame
from pubsub import pub

class CheckAlienGotShot(BaseListener):

    def __init__(self, app):
        self.app = app

    def handle(self):
        collisions = pygame.sprite.groupcollide(
            self.app.ship.bullets,
            self.app.fleet.aliens,
            True,
            True
        )

        if collisions:
            pub.sendMessage(
                'aliens-killed',
                app=self.app,
                collisions=collisions
            )

    def build(app):
        listener = CheckAlienGotShot(app)
        listener()