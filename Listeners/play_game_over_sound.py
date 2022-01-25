from Listeners.base_listener import BaseListener
import pygame

class PlayGameOverSound(BaseListener):
    def __init__(self, app):
        self.app = app      

    def handle(self):
        if self.app.stats.is_active():
            effect = pygame.mixer.Sound('Sounds/gameover.wav')
            effect.play()

    def build(app):
        listener = PlayGameOverSound(app)
        listener()