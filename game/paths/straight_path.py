class StraightPath:
    def __init__(self, bullet_speed = 3.0, bullet_horizontal_speed = 0):
        self.bullet_speed = bullet_speed
        self.bullet_horizontal_speed = bullet_horizontal_speed

    def calculate(self, bullet):
        bullet.y -= self.bullet_speed
        bullet.x += self.bullet_horizontal_speed
        bullet.rect.y = bullet.y
        bullet.rect.x = bullet.x
