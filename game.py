import pygame
import random
from grid import *
from blocks import *

class Game():
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0

        self.rotate_sound = pygame.mixer.Sound("Sounds/rotate.ogg")
        self.clear_sound = pygame.mixer.Sound("Sounds/clear.ogg")
        self.background_music = pygame.mixer.Sound("Sounds/music.ogg")
        self.background_music.play(-1)

    #update the score of the game
    def update_score(self,lines_clear,move_down_points):
        if lines_clear == 1:
            self.score += 100
        elif lines_clear == 2:
            self.score += 250
        elif lines_clear == 3:
            self.score += 500
        elif lines_clear == 4:
            self.score += 1000
        self.score += move_down_points

    #return a random block
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    #move the block left,right and down
    def move_left(self):
        self.current_block.move(0,-1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0,1)

    def move_right(self):
        self.current_block.move(0,1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0,-1)

    def move_down(self):
        self.current_block.move(1,0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1,0)
            self.lock_block()
    
    #lock down the block after it touch the bottom
    def lock_block(self):
        tiles = self.current_block.get_cell_position()
        for position in tiles:
            self.grid.grid[position.row][position.col] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_clear = self.grid.clear_full_rows()
        if rows_clear > 0:
            self.clear_sound.play()
            self.update_score(rows_clear,0)
        if self.block_fits() == False:
            self.game_over = True
            self.background_music.stop()

    #check if the block fits in the empty space
    def block_fits(self):
        tiles = self.current_block.get_cell_position()
        for tile in tiles:
            if self.grid.is_empty(tile.row,tile.col) == False:
                return False
        return True

    #rotate the block
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()
        else:
            self.rotate_sound.play()

    #check if the block is inside the boundary
    def block_inside(self):
        tiles = self.current_block.get_cell_position()
        for tile in tiles:
            if self.grid.is_inside(tile.row,tile.col) == False:
                return False
        return True
    
    #reset the game after the game is over and restart again
    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
        self.background_music.play(-1)
    
    #draw the block on the screen
    def draw(self,screen):
        self.grid.draw(screen)
        self.current_block.draw(screen,11,11)
        if self.next_block.id == 3:
            self.next_block.draw(screen,255,290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen,255,280)
        else:
            self.next_block.draw(screen,270,270)