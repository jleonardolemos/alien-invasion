from Listeners.base_listener import BaseListener
import pygame

class ShipMovement(BaseListener):

    def __init__(self, event_key, event_type, ship):
        self.ship = ship
        self.event_key = event_key
        self.event_type = event_type

    def handle(self):
        if self.event_type == pygame.KEYDOWN:
            if self.event_key  == pygame.K_RIGHT:
                self.ship.startMovingRight()
            elif self.event_key == pygame.K_LEFT:
                self.ship.startMovingLeft()

        elif self.event_type == pygame.KEYUP:        
            if self.event_key == pygame.K_RIGHT: 
                self.ship.stopMovingRight()
            elif self.event_key == pygame.K_LEFT:
                self.ship.stopMovingLeft()

    def build(event, app=None):
        listener = ShipMovement(event.key, event.type, app.ship)
        listener()