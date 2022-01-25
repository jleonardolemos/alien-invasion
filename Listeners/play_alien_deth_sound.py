from Listeners.base_listener import BaseListener
import pygame

class PlayAlienDethSound(BaseListener):
    def handle(self):
        effect = pygame.mixer.Sound('Sounds/invaderkilled.wav')
        effect.play()

    def build(app, collisions=None):
        listener = PlayAlienDethSound()
        listener()