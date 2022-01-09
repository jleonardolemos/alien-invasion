from pubsub import pub
import pygame
from Listeners.play_button import PlayButton
from Listeners.quit_listener import QuitListener
from Listeners.reset_game_stats import ResetGameStats
from Listeners.ship_movement import ShipMovement

class EventMap:
    def __init__(self, ai_game):
        self.ship = ai_game.ship
        pub.subscribe(QuitListener.build, "event-" + str(pygame.QUIT))
        pub.subscribe(QuitListener.build, "event-" + str(pygame.KEYDOWN) + "." + str(pygame.K_q))
        pub.subscribe(ShipMovement.build, "event-" + str(pygame.KEYDOWN))
        pub.subscribe(ShipMovement.build, "event-" + str(pygame.KEYUP))
        pub.subscribe(PlayButton.build, "event-" + str(pygame.MOUSEBUTTONDOWN))
        pub.subscribe(ResetGameStats.build, "play")