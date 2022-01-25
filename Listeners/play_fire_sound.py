from Listeners.base_listener import BaseListener
import pygame

class PlayFireSound(BaseListener):
    def handle(self):
        effect = pygame.mixer.Sound('Sounds/shoot.wav')
        effect.play()

    def build(event, app=None):
        listener = PlayFireSound()
        listener()