from Listeners.base_listener import BaseListener
from pubsub import pub

class LevelUp(BaseListener):

    def __init__(self, app):
        self.app = app

    def handle(self):
        if not self.app.fleet.aliens:
            self.app.gun.clean_bullets()
            self.app.fleet.create()
            self.app.settings.increase_speed()
            self.app.stats.level += 1
            self.app.sb.prep_level()
            pub.sendMessage('level-up', app = self.app)

    def build(app, collisions=None):
        listener = LevelUp(app)
        listener()