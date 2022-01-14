import pygame.font

from drawable import Drawable

class Button(Drawable):
    def __init__(self, ai_game, msg):
        self.stats = ai_game.stats
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        screen_rect = ai_game.screen.get_rect()
        self.rect.center = screen_rect.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(
            msg,
            True,
            self.text_color,
            self.button_color
        )

        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self, screen):
        if not self.stats.is_active():
            screen.fill(self.button_color, self.rect)
            screen.blit(self.msg_image, self.msg_image_rect)