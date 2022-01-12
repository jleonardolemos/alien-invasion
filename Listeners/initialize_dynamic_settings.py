from Listeners.base_listener import BaseListener

class InitializeDynamicSettings(BaseListener):

    def __init__(self, settings):
        self.settings = settings

    def handle(self):
        self.settings.initialize_dynamic_settings()

    def build(event, app=None):
        listener = InitializeDynamicSettings(app.settings)
        listener()