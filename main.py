import pygame
from alien_invasion import AlienInvasion
from game_state import GameState
from menus.main_menu import MainMenu
from settings import Settings

settings = Settings()
game_state = GameState()

surface = pygame.display.set_mode((
    settings.screen_width,
    settings.screen_height
), pygame.NOFRAME)

ai = AlienInvasion(game_state, settings, surface)
main_menu = MainMenu(game_state, surface, settings)

pygame.mouse.set_visible(False)

while True:
    if game_state.has_game_just_started():
        main_menu.game_loop()
    else:
        ai.game_loop()