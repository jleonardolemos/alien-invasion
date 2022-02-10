from Listeners.base_listener import BaseListener

class RemoveLostBullet(BaseListener):

    def __init__(self, app):
        self.app = app

    def handle(self):
        for bullet in self.app.gun.get_bullets_copy():
            if bullet.rect.bottom <= 0:
                self.app.gun.remove_bullet(bullet)

    def build(app):
        listener = RemoveLostBullet(app)
        listener()