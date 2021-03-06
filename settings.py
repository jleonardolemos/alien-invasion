from os import path, makedirs

class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self, settings_dir="~"):
        self.settings_dir = settings_dir
        self.__load_config(self.settings_dir)

        """Initialize the game's settings."""
        # Player settings
        self.player_name = ""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bg_image = 'images/background.bmp'

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
    
    def __load_config(self, settings_dir = "~"):
        dir = path.expanduser(self.settings_dir) + "/l30/alien"
        makedirs(dir, exist_ok=True)