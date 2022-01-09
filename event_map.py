from pubsub import pub
import pygame
from Listeners.quit_listener import QuitListener
from Listeners.ship_movement import ShipMovement

class EventMap:
    def __init__(self, ai_game):
        self.ship = ai_game.ship
        pub.subscribe(QuitListener.build, "event-" + str(pygame.QUIT))
        pub.subscribe(QuitListener.build, "event-" + str(pygame.KEYDOWN) + "." + str(pygame.K_q))
        pub.subscribe(ShipMovement.build, "event-" + str(pygame.KEYDOWN))
        pub.subscribe(ShipMovement.build, "event-" + str(pygame.KEYUP))