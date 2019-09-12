import pygame as pg
import uuid

class Maze:

    def __init__(self, screen):
        self.group_of_cells = []
        SIZE = 4
        x = 0
        y = 0
        for i in range(SIZE):
            self.group_of_cells.append([])
            for j in range(SIZE):
                self.group_of_cells[i].append(Cell(screen, (255,255,255), x, y))
                x += 100
            x = 0
            y += 100
        # print(self.group_of_cells)
        # self.r = pg.draw.rect(screen, (0,0,0), pg.Rect(0,0,100,100), 2 )
        # self.inner_r = pg.draw.rect(screen, (255,255,255), pg.Rect(2,2,97,97) )




class Cell:

    def __init__(self, screen, custom_color, x, y):
        self.source = False
        self.target = False
        self.wall = False
        self.color = custom_color
        self.unique_ID = uuid.uuid4()
        self.r = pg.draw.rect(screen, (0, 0, 0), pg.Rect(x, y, 100, 100), 2)
        self.inner_r = pg.draw.rect(screen, self.color, pg.Rect(x+2, y+2, 97, 97))

    def Source(self):
        self.source = True
        self.target = False
        # print(self.source) #, self.target)

    def Target(self):
        self.target = True
        self.source = False
        # print(self.target) #, self.target)

    def cancel(self):
        self.target = False
        self.source = False
        # print(self.source) #, self.target)

    def build_wall(self):
        self.wall = True
        # print("you just BUID a wall")

    def destroy_wall(self):
        self.wall = False
        # print("you just DESTROY a wall")

    def get_ID(self):
        return self.unique_ID


    def change_color(self, screen, c, x, y):
        self.inner_r = pg.draw.rect(screen, c, pg.Rect(x+2, y+2, 97, 97))
