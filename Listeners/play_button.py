from Listeners.base_listener import BaseListener
import pygame
from pubsub import pub

class PlayButton(BaseListener):

    def __init__(self, play_button, game_active, app):
        self.play_button = play_button
        self.game_active = game_active
        self.app = app

    def handle(self):
        mouse_pos = pygame.mouse.get_pos()
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            pub.sendMessage("play", event="play", app=self.app)
        
        pygame.mouse.set_visible(False)

    def build(event, app=None):
        listener = PlayButton(app.play_button, app.stats.is_active(), app)
        listener()