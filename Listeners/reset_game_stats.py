from Listeners.base_listener import BaseListener

class ResetGameStats(BaseListener):

    def __init__(self, stats):
        self.stats = stats        

    def handle(self):
        self.stats.reset_stats()
        self.stats.active()

    def build(app=None):
        listener = ResetGameStats(app.stats)
        listener()