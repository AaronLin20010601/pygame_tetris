import pygame
from colors import *
from position import *

class Block:
    #block initialize
    def __init__(self,id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.col_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    #move the block on the screen
    def move(self,rows,cols):
        self.row_offset += rows
        self.col_offset += cols

    #return cell position
    def get_cell_position(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset,position.col + self.col_offset)
            moved_tiles.append(position)
        return moved_tiles

    #rotate the block
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    #undo the rotation if block move outside the window after rotation
    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1

    #draw the block on the screen
    def draw(self,screen,offset_x,offset_y):
        tiles = self.get_cell_position()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.col * self.cell_size,offset_y + tile.row * self.cell_size,self.cell_size - 1,self.cell_size - 1)
            pygame.draw.rect(screen,self.colors[self.id],tile_rect)