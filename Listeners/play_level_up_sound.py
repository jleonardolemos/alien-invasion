from Listeners.base_listener import BaseListener
import pygame
import random

class PlayLevelUpSound(BaseListener):
    def handle(self):
        sounds = [
            'Sounds/hellyeah.wav',
            'Sounds/keepgoing.wav',
            'Sounds/great.wav',
        ]

        effect = pygame.mixer.Sound(random.choice(sounds))
        effect.play()

    def build(app):
        listener = PlayLevelUpSound()
        listener()