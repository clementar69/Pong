from pygame import Vector2
import core

class rectangle2:
    def __init__(self):
        self.périmetre=(1500, 400, 40, 250)
        self.couleur=(150, 150, 150)
        self.direction = Vector2(0, 0)

    def deplacement2(self,o,l):

        if o:
            self.direction = Vector2(self.direction.x, -1)
        if l:
            self.direction = Vector2(self.direction.x, 1)

    def limit(self):
        core.WINDOW_SIZE = [1600, 900]

        if self.position.y < 0 or self.position.y > core.WINDOW_SIZE[1]:
            self.direction, Vector2(self.direction.x, self.direction.y * -1)

        if self.position.x < 0 or self.position.x > core.WINDOW_SIZE[0]:
            self.direction, Vector2(self.direction.x * -1, self.direction.y)

