import pygame_menu
from pygame_menu import Theme
from menus.theme_builder import ThemeBuilder

class StartMenu:

    def __init__(self, game_state, surface, settings):
        self.game_state = game_state
        self.surface = surface
        self.settings = settings

        self.menu = pygame_menu.Menu(
            width=self.settings.screen_width,
            height=self.settings.screen_height,
            theme=ThemeBuilder.buld_default_theme(),
            title=None,
        )

        self.menu.add.button('Continue', self.start_the_game)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

    def game_loop(self):
        self.menu.enable()
        self.menu.mainloop(self.surface)

    def start_the_game(self) -> None:
        self.game_state.run_game()
        self.menu.disable()

    def exit_menu(self):
        self.game_state.run_game()
        pygame_menu.events.EXIT()