import sys

from Listeners.base_listener import BaseListener

class QuitListener(BaseListener):

    def handle(self):
        sys.exit()

    def build(event, app=None):
        listener = QuitListener()
        listener()