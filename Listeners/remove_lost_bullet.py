from Listeners.base_listener import BaseListener

class RemoveLostBullet(BaseListener):

    def __init__(self, app):
        self.app = app

    def handle(self):
        for bullet in self.app.gun.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.app.gun.bullets.remove(bullet)

    def build(app):
        listener = RemoveLostBullet(app)
        listener()