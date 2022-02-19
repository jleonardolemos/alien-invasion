class GameState:
    def __init__(self):
        self.__state = 'start'
    def run_game(self):
        self.__state = 'running'
    def pause_game(self):
        self.__state = 'start'
    def is_game_running(self):
        return self.__state == 'running'
    def has_game_just_started(self):
        return self.__state == 'start'