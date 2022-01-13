from Listeners.base_listener import BaseListener
from fleet import Fleet

class CreateFleet(BaseListener):

    def __init__(self, fleet):
        self.fleet = fleet

    def handle(self):
        self.fleet.create()

    def build(event, app=None):
        listener = CreateFleet(app.fleet)
        listener()