from Listeners.base_listener import BaseListener
from game.guns.spread_gun import SpreadGun

class UpgradeGun(BaseListener):

    def __init__(self, app):
        self.app = app

    def handle(self):
        self.app.change_gun(SpreadGun(self.app));

    def build(event, app=None):
        listener = UpgradeGun(app)
        listener()