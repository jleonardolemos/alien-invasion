from Listeners.base_listener import BaseListener
from pubsub import pub

class Pause(BaseListener):

    def __init__(self, app):
        self.app = app

    def handle(self):
        self.app.game_state.pause_game()

    def build(event, app=None):
        listener = Pause(app)
        listener()