from pygame import Vector2
import core

class rectangle:
    def __init__(self):
        self.périmetre=(60, 400, 40, 250)
        self.couleur=(150, 150, 150)
        self.direction = Vector2(0, 0)

    def deplacement(self,z,s):

        if z:
            self.direction = Vector2(self.direction.x, -1)
        if s:
            self.direction = Vector2(self.direction.x, 1)

    def limit(self):
        core.WINDOW_SIZE = [1600, 900]

        if self.position.y < 0 or self.position.y > core.WINDOW_SIZE[1]:
            self.direction, Vector2(self.direction.x, self.direction.y * -1)

        if self.position.x < 0 or self.position.x > core.WINDOW_SIZE[0]:
            self.direction, Vector2(self.direction.x * -1, self.direction.y)
