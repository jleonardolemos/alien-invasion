import sys

from Listeners.base_listener import BaseListener

class QuitListener(BaseListener):

    def handle(self):
        sys.exit()