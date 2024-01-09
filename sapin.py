import random
from collections import namedtuple

import pygame as pg

pg.init()

screen = pg.display.set_mode( (480, 640) )

image = pg.image.load('sapin.png')
screen.blit(image, (0, 0))
pg.display.flip()

clock = pg.time.Clock()

running = True

# ici 1
Circle = namedtuple('Circle', ['x', 'y', 'radius', 'color'])
# Circle(10,10,30,(255,0,0))


figures = []

while running:
    clock.tick(20)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONUP:
            x,y = pg.mouse.get_pos()
            figures.append(Circle(x=x, y=y, radius=20, color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))

    for fig in figures:
        # ici 2
        pg.draw.circle(screen, fig.color, (fig.x, fig.y), fig.radius)


    pg.display.update()
