from Listeners.base_listener import BaseListener

class IncreaseScoreByAlienKilled(BaseListener):

    def __init__(self, app, collisions):
        self.collisions = collisions
        self.app = app

    def handle(self):
        for aliens in self.collisions.values():
            self.app.stats.score += self.app.settings.alien_points * len(aliens)

        self.app.sb.prep_score()
        self.app.sb.check_high_score()


    def build(app, collisions=None):
        listener = IncreaseScoreByAlienKilled(app, collisions)
        listener()