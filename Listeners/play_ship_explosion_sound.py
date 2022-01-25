from Listeners.base_listener import BaseListener
import pygame

class PlayShipExplosionSound(BaseListener):
    def __init__(self, app):
        self.app = app       

    def handle(self):
        if self.app.stats.is_active():
            effect = pygame.mixer.Sound('Sounds/explosion.wav')
            effect.play()

    def build(app):
        listener = PlayShipExplosionSound(app)
        listener()