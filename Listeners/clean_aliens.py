from Listeners.base_listener import BaseListener

class CleanAliens(BaseListener):

    def __init__(self, alien_group):
        self.alien_group = alien_group

    def handle(self):
        self.alien_group.empty();

    def build(event, app=None):
        listener = CleanAliens(app.aliens)
        listener()