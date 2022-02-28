from Listeners.base_listener import BaseListener

class CentralizeShip(BaseListener):

    def __init__(self, ship):
        self.ship = ship

    def handle(self):
        self.ship.center_ship();

    def build(app=None):
        listener = CentralizeShip(app.ship)
        listener()