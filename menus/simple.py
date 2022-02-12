"""
pygame-menu
https://github.com/ppizarror/pygame-menu

EXAMPLE - SIMPLE
Super simple example of pygame-menu usage, featuring a selector and a button.
"""

import pygame_menu
from pygame_menu.examples import create_example_window
from pygame_menu import Theme

from typing import Tuple, Any

surface = create_example_window('Example - Simple', (1600, 1200))


def set_difficulty(selected: Tuple, value: Any) -> None:
    """
    Set the difficulty of the game.
    """
    print(f'Set difficulty to {selected[0]} ({value})')


def start_the_game() -> None:
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    global user_name
    print(f'{user_name.get_value()}, Do the job here!')

mytheme = Theme(background_color=(0, 0, 0, 0), # transparent background
                title_background_color=(4, 47, 126),
                title_font_shadow=True,
                # widget_font=pygame_menu.font.FONT_DIGITAL,
                widget_font=pygame_menu.font.FONT_8BIT,
                widget_padding=25,
                title=False,
                # widget_font_antialias=True,
                title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE)

menu = pygame_menu.Menu(
    height=1200,
    theme=mytheme,
    title=None,
    width=1600
)

user_name = menu.add.text_input('Name: ', default='John Doe', maxchar=10)
menu.add.selector('Difficulty: ', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)
