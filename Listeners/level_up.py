from Listeners.base_listener import BaseListener

class LevelUp(BaseListener):

    def __init__(self, app):
        self.app = app

    def handle(self):
        if not self.app.fleet.aliens:
            self.app.ship.bullets.empty()
            self.app.fleet.create()
            self.app.settings.increase_speed()
            self.app.stats.level += 1
            self.app.sb.prep_level()

    def build(app, collisions=None):
        listener = LevelUp(app)
        listener()