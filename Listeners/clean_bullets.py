from Listeners.base_listener import BaseListener

class CleanBullets(BaseListener):

    def __init__(self, ship):
        self.ship = ship

    def handle(self):
        self.ship.clean_bullets();

    def build(event, app=None):
        listener = CleanBullets(app.ship)
        listener()