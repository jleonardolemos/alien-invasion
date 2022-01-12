from Listeners.base_listener import BaseListener
from ship import Ship

class FireBullet(BaseListener):

    def __init__(self, app):
        self.app = app

    def handle(self):
        Ship.fire(self.app)

    def build(event, app=None):
        listener = FireBullet(app)
        listener()