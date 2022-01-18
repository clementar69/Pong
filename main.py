import core
import pygame
import pygame.draw
from rectangle2 import rectangle2
from rectangle import rectangle
from balle import balle
from pygame import Vector2

def setup():

    core.fps = 60
    core.WINDOW_SIZE = [1600, 900]

    core.memory("rectangle", rectangle())
    core.memory("rectangle2",rectangle2())



    core.memory("TableauDeRectangle", [])
    for r in range(1):
        core.memory("TableauDeRectangle").append(rectangle())



    core.memory("TableauDeRectangle2", [])
    for r2 in range(1):
        core.memory("TableauDeRectangle2").append(rectangle2())



    core.memory("TableauDeBalle", [])
    for b in range(1):
        core.memory("TableauDeBalle").append(balle())








def run():
    core.cleanScreen()


    for r in core.memory("TableauDeRectangle"):
       pygame.draw.rect(core.screen, r.couleur , r.périmetre ,)


    for r2 in core.memory("TableauDeRectangle2"):
       pygame.draw.rect(core.screen, r2.couleur , r2.périmetre ,)

    for b in core.memory("TableauDeBalle"):
        pygame.draw.circle(core.screen, b.couleur, b.position ,b.rayon)

    if core.getKeyPressList("z"):
        core.memory("direction", Vector2(core.memory("direction").x, -1))

    if core.getKeyPressList("s"):
        core.memory("direction", Vector2(core.memory("direction").x, 1))




core.main(setup, run)







