from Listeners.base_listener import BaseListener
from pubsub import pub

class CheckAliensBottom(BaseListener):

    def __init__(self, app):
        self.app = app

    def handle(self):
        screen_rect = self.app.screen.get_rect()
        for alien in self.app.fleet.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                pub.sendMessage('ship-hit', app=self.app)
                break

    def build(app):
        listener = CheckAliensBottom(app)
        listener()