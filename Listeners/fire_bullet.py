from Listeners.base_listener import BaseListener

class FireBullet(BaseListener):

    def __init__(self, gun):
        self.gun = gun

    def handle(self):
        self.gun.fire()

    def build(event, app=None):
        listener = FireBullet(app.gun)
        listener()