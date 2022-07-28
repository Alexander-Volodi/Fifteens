import pygame as pg
import sys
from random import randint

pg.init()
BACK_GROUND = (150, 150, 150)

coordinates = {}
fifteens_table = [[0] * 4 for i in range(4)]
for i in range(1, 16):
    coordinate = randint(0, 15)
    while coordinate in coordinates:
        coordinate = randint(0, 15)
    coordinates[coordinate] = i
for i in range(4):
    for j in range(4):
        if i * 4 + j in coordinates:
            fifteens_table[i][j] = coordinates[i * 4 + j]
        else:
            fifteens_table[i][j] = 0

fifteens_surf = pg.display.set_mode((400, 400))
fifteens_surf.fill(BACK_GROUND)
pg.display.set_caption('Fifteens')
pg.display.update()

numbers_font = pg.font.Font(None, 36)

for i in range(4):
    for j in range(4):
        if fifteens_table[i][j]:
            numbers_text = numbers_font.render(str(fifteens_table[i][j]), True,
                              (40, 40, 40))
            fifteens_surf.blit(numbers_text, (i * 100 + 40, j * 100 + 40))

pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            pass
