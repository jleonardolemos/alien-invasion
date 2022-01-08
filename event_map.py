from pubsub import pub
import pygame
from Listeners.quit_listener import QuitListener

def quit_listener_caller(event=None):
    quit_listener = QuitListener()
    quit_listener(event)

class EventMap:

    def __init__(self):
        pub.subscribe(quit_listener_caller, "event-" + str(pygame.QUIT))
