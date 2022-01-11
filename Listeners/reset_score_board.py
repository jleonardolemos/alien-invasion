from Listeners.base_listener import BaseListener

class ResetScoreBoard(BaseListener):

    def __init__(self, sb):
        self.sb = sb        

    def handle(self):
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

    def build(event, app=None):
        listener = ResetScoreBoard(app.sb)
        listener()