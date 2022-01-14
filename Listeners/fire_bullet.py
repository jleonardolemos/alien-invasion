from Listeners.base_listener import BaseListener

class FireBullet(BaseListener):

    def __init__(self, ship):
        self.ship = ship

    def handle(self):
        self.ship.fire()

    def build(event, app=None):
        listener = FireBullet(app.ship)
        listener()