import pygame
from colors import *

class Grid:
    #grid initialize
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()
    
    #print out grid number of value in console
    def print_grid(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col],end = " ")
            print()

    #check if the block is out of game boundary
    def is_inside(self,row,col):
        if row >= 0 and row < self.num_rows and col >= 0 and col < self.num_cols:
            return True
        return False
    
    #check if the block touch the other block already exist
    def is_empty(self,row,col):
        if self.grid[row][col] == 0:
            return True
        return False

    #check if there is row is full
    def is_row_full(self,row):
        for col in range(self.num_cols):
            if self.grid[row][col] == 0:
                return False
        return True
    
    #clear the full row and remove it
    def clear_row(self,row):
        for col in range(self.num_cols):
            self.grid[row][col] = 0

    #move the row down after clear the full row
    def move_row_down(self,row,num_rows):
        for col in range(self.num_cols):
            self.grid[row + num_rows][col] = self.grid[row][col]
            self.grid[row][col] = 0
    
    #check all the full rows and clear them,then move down all the uncomplete row down
    def clear_full_rows(self):
        complete = 0
        for row in range(self.num_rows - 1,0,-1):
            if self.is_row_full(row):
                self.clear_row(row)
                complete += 1
            elif complete > 0:
                self.move_row_down(row,complete)
        return complete

    #reset the grid after the game is over and restart again
    def reset(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.grid[row][col] = 0

    #draw the color of cell on the corresponding block location
    def draw(self,screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col * self.cell_size + 11,row * self.cell_size + 11,self.cell_size - 1,self.cell_size - 1)
                pygame.draw.rect(screen,self.colors[cell_value],cell_rect)