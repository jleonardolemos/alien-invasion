from Listeners.base_listener import BaseListener

class CleanBullets(BaseListener):

    def __init__(self, bullets_group):
        self.bullets_group = bullets_group

    def handle(self):
        self.bullets_group.empty();

    def build(event, app=None):
        listener = CleanBullets(app.bullets)
        listener()