from pubsub import pub
import pygame
from Listeners.centralize_ship import CentralizeShip
from Listeners.clean_aliens import CleanAliens
from Listeners.clean_bullets import CleanBullets
from Listeners.create_fleet import CreateFleet
from Listeners.fire_bullet import FireBullet
from Listeners.initialize_dynamic_settings import InitializeDynamicSettings
from Listeners.play_button import PlayButton
from Listeners.quit_listener import QuitListener
from Listeners.reset_game_stats import ResetGameStats
from Listeners.reset_score_board import ResetScoreBoard
from Listeners.ship_movement import ShipMovement

class EventMap:
    def __init__(self, ai_game):
        self.ship = ai_game.ship
        pub.subscribe(QuitListener.build, "event-" + str(pygame.QUIT))
        pub.subscribe(QuitListener.build, "event-" + str(pygame.KEYDOWN) + "." + str(pygame.K_q))
        pub.subscribe(ShipMovement.build, "event-" + str(pygame.KEYDOWN))
        pub.subscribe(ShipMovement.build, "event-" + str(pygame.KEYUP))
        pub.subscribe(PlayButton.build, "event-" + str(pygame.MOUSEBUTTONDOWN))
        pub.subscribe(FireBullet.build, "event-" + str(pygame.KEYDOWN) + "." + str(pygame.K_SPACE))
        pub.subscribe(ResetGameStats.build, "play")
        pub.subscribe(ResetScoreBoard.build, "play")
        pub.subscribe(CleanAliens.build, "play")
        pub.subscribe(CleanBullets.build, "play")
        pub.subscribe(CreateFleet.build, "play")
        pub.subscribe(CentralizeShip.build, "play")
        pub.subscribe(InitializeDynamicSettings.build, "play")