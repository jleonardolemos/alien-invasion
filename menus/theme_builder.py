from abc import ABC, abstractmethod
import pygame_menu
from pygame_menu import Theme

class ThemeBuilder(ABC):

    @abstractmethod
    def buld_default_theme():
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