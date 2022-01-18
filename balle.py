
from pygame import Vector2

class balle:
    def __init__(self):
        self.rayon=12
        self.couleur=(250, 250, 250)
        self.position=Vector2(800, 450)
        self.direction = Vector2(0, 0)