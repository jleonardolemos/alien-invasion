from Listeners.base_listener import BaseListener
from fleet import Fleet

class CreateFleet(BaseListener):

    def __init__(self, app):
        self.app = app

    def handle(self):
        Fleet.create(self.app)

    def build(event, app=None):
        listener = CreateFleet(app)
        listener()