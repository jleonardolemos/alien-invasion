from Listeners.base_listener import BaseListener

class CleanAliens(BaseListener):

    def __init__(self, fleet):
        self.fleet = fleet

    def handle(self):
        self.fleet.clean();

    def build(event, app=None):
        listener = CleanAliens(app.fleet)
        listener()