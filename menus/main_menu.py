from abc import abstractmethod
import pygame_menu
from pygame_menu import Theme

class MainMenu:

    def __init__(self, game_state, surface, settings):
        self.game_state = game_state
        self.surface = surface
        self.settings = settings

        self.menu = pygame_menu.Menu(
            width=self.settings.screen_width,
            height=self.settings.screen_height,
            theme=MainMenu.buld_theme(),
            title=None,
        )

        self.txt_user_name = self.menu.add.text_input('Name: ', default='Mandalorian', maxchar=20)
        self.menu.add.selector('Difficulty: ', [('Hard', 1), ('Easy', 2)])
        self.menu.add.button('Play', self.start_the_game)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

    def game_loop(self):
        self.menu.enable()
        self.menu.mainloop(self.surface)

    def start_the_game(self) -> None:
        self.settings.player_name = self.txt_user_name.get_value()
        self.game_state.run_game()
        self.menu.disable()

    def exit_menu(self):
        self.game_state.run_game()
        pygame_menu.events.EXIT()

    @abstractmethod
    def buld_theme():
        mytheme = Theme(background_color=(0, 0, 0, 0), # transparent background
                title_background_color=(4, 47, 126),
                title_font_shadow=True,
                # widget_font=pygame_menu.font.FONT_DIGITAL,
                widget_font=pygame_menu.font.FONT_8BIT,
                widget_padding=25,
                title=False,
                # widget_font_antialias=True,
                title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE)

        return mytheme