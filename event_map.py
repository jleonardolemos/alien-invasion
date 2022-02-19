from pubsub import pub
import pygame
from Listeners.centralize_ship import CentralizeShip
from Listeners.check_alien_got_shot import CheckAlienGotShot
from Listeners.check_aliens_bottom import CheckAliensBottom
from Listeners.check_ship_hit import CheckShipHit
from Listeners.clean_aliens import CleanAliens
from Listeners.clean_bullets import CleanBullets
from Listeners.create_fleet import CreateFleet
from Listeners.die import Die
from Listeners.fire_bullet import FireBullet
from Listeners.increase_score_by_alien_killed import IncreaseScoreByAlienKilled
from Listeners.initialize_dynamic_settings import InitializeDynamicSettings
from Listeners.level_up import LevelUp
from Listeners.play_alien_deth_sound import PlayAlienDethSound
from Listeners.play_fire_sound import PlayFireSound
from Listeners.play_game_over_sound import PlayGameOverSound
from Listeners.play_level_up_sound import PlayLevelUpSound
from Listeners.play_ship_explosion_sound import PlayShipExplosionSound
from Listeners.quit_listener import QuitListener
from Listeners.remove_lost_bullet import RemoveLostBullet
from Listeners.reset_game_stats import ResetGameStats
from Listeners.reset_score_board import ResetScoreBoard
from Listeners.ship_movement import ShipMovement
from game.listeners.upgrade_gun import UpgradeGun

class EventMap:
    def __init__(self, ai_game):
        self.ship = ai_game.ship
        pub.subscribe(QuitListener.build, "event-" + str(pygame.QUIT))
        pub.subscribe(QuitListener.build, "event-" + str(pygame.KEYDOWN) + "." + str(pygame.K_q))
        pub.subscribe(ShipMovement.build, "event-" + str(pygame.KEYDOWN))
        pub.subscribe(ShipMovement.build, "event-" + str(pygame.KEYUP))
        pub.subscribe(FireBullet.build, "event-" + str(pygame.KEYDOWN) + "." + str(pygame.K_SPACE))
        pub.subscribe(PlayFireSound.build, "event-" + str(pygame.KEYDOWN) + "." + str(pygame.K_SPACE))
        pub.subscribe(UpgradeGun.build, "event-" + str(pygame.KEYDOWN) + "." + str(pygame.K_a))
        pub.subscribe(CheckAlienGotShot.build, "move-completed")
        pub.subscribe(CheckShipHit.build, "move-completed")
        pub.subscribe(CheckAliensBottom.build, "move-completed")
        pub.subscribe(RemoveLostBullet.build, "move-completed")
        pub.subscribe(IncreaseScoreByAlienKilled.build, "aliens-killed")
        pub.subscribe(PlayAlienDethSound.build, "aliens-killed")
        pub.subscribe(LevelUp.build, "aliens-killed")
        pub.subscribe(PlayShipExplosionSound.build, "ship-hit")
        pub.subscribe(Die.build, "ship-hit")
        pub.subscribe(PlayGameOverSound.build, "game-over")
        pub.subscribe(ResetGameStats.build, "game-over")
        pub.subscribe(ResetScoreBoard.build, "game-over")
        pub.subscribe(CleanAliens.build, "game-over")
        pub.subscribe(CleanBullets.build, "game-over")
        pub.subscribe(CreateFleet.build, "game-over")
        pub.subscribe(CentralizeShip.build, "game-over")
        pub.subscribe(InitializeDynamicSettings.build, "game-over")
        pub.subscribe(PlayLevelUpSound.build, "level-up")