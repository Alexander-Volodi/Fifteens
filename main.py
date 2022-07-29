import pygame as pg
import sys
from random import randint

pg.init()
BACK_GROUND = (180, 180, 180)

coordinates = {}
colors = [(190, 170, 210), (160, 220, 220), (220, 220, 160), (210, 150, 150), (170, 220, 170), (220, 190, 160),
          (160, 170, 220), (140, 190, 220), (120, 180, 170), (220, 160, 220), (220, 140, 100), (200, 160, 160),
          (160, 130, 200), (220, 220, 220), (180, 100, 190)]
colors_for_rects = dict(zip(range(1, 16), colors))
fifteens_table = [[0] * 4 for i in range(4)]
indexes = []
for i in range(1, 16):
    coordinate = randint(0, 15)
    indexes.append(i)
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
            pg.draw.rect(fifteens_surf, colors_for_rects[fifteens_table[i][j]], (i * 100, j * 100, 100, 100),
                         border_radius=10)
            numbers_text = numbers_font.render(str(fifteens_table[i][j]), True,
                              (40, 40, 40))
            fifteens_surf.blit(numbers_text, (i * 100 + 40, j * 100 + 40))

pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            coordinate_mouse_x = event.pos[0] // 100
            coordinate_mouse_y = event.pos[1] // 100
            if fifteens_table[coordinate_mouse_x][coordinate_mouse_y]:
                if 0 < coordinate_mouse_x:
                    if not fifteens_table[coordinate_mouse_x - 1][coordinate_mouse_y]:
                        fifteens_table[coordinate_mouse_x][coordinate_mouse_y], fifteens_table[coordinate_mouse_x - 1][coordinate_mouse_y] = \
                        fifteens_table[coordinate_mouse_x - 1][coordinate_mouse_y], fifteens_table[coordinate_mouse_x][coordinate_mouse_y]
                if coordinate_mouse_x < 3:
                    if not fifteens_table[coordinate_mouse_x + 1][coordinate_mouse_y]:
                        fifteens_table[coordinate_mouse_x][coordinate_mouse_y], fifteens_table[coordinate_mouse_x + 1][coordinate_mouse_y] = \
                        fifteens_table[coordinate_mouse_x + 1][coordinate_mouse_y], fifteens_table[coordinate_mouse_x][coordinate_mouse_y]
                if 0 < coordinate_mouse_y:
                    if not fifteens_table[coordinate_mouse_x][coordinate_mouse_y - 1]:
                        fifteens_table[coordinate_mouse_x][coordinate_mouse_y], fifteens_table[coordinate_mouse_x][coordinate_mouse_y - 1] = \
                        fifteens_table[coordinate_mouse_x][coordinate_mouse_y - 1], fifteens_table[coordinate_mouse_x][coordinate_mouse_y]
                if coordinate_mouse_y < 3:
                    if not fifteens_table[coordinate_mouse_x][coordinate_mouse_y + 1]:
                        fifteens_table[coordinate_mouse_x][coordinate_mouse_y], fifteens_table[coordinate_mouse_x][coordinate_mouse_y + 1] = \
                        fifteens_table[coordinate_mouse_x][coordinate_mouse_y + 1], fifteens_table[coordinate_mouse_x][coordinate_mouse_y]
            fifteens_surf.fill(BACK_GROUND)
            for i in range(4):
                for j in range(4):
                    if fifteens_table[i][j]:
                        pg.draw.rect(fifteens_surf, colors_for_rects[fifteens_table[i][j]],
                                     (i * 100, j * 100, 100, 100),
                                     border_radius=10)
                        numbers_text = numbers_font.render(str(fifteens_table[i][j]), True,
                                                           (40, 40, 40))
                        fifteens_surf.blit(numbers_text, (i * 100 + 40, j * 100 + 40))
            pg.display.update()
