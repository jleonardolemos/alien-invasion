from Listeners.base_listener import BaseListener

class CleanBullets(BaseListener):

    def __init__(self, gun):
        self.gun = gun

    def handle(self):
        self.gun.clean_bullets();

    def build(app=None):
        listener = CleanBullets(app.gun)
        listener()