from alien_invasion import AlienInvasion
from game_state import GameState
from menus.main_menu import MainMenu
from settings import Settings

settings = Settings()
game_state = GameState()
ai = AlienInvasion(game_state, settings)
main_menu = MainMenu(game_state, ai.screen, settings)

while True:
    if game_state.has_game_just_started():
        main_menu.game_loop()
    else:
        ai.game_loop()