class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.__game_active = False
        self.high_score = 0
    
    def active(self):
        self.__game_active = True

    def inactive(self):
        self.__game_active = False

    def is_active(self):
        return self.__game_active

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1