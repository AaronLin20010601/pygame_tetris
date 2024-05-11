import pygame,sys
from game import *
from colors import *

#initialize
pygame.init()
title_font = pygame.font.Font(None,40)
score_surface = title_font.render("Score",True,Colors.white)
next_surface = title_font.render("Next",True,Colors.white)
game_over_surface = title_font.render("GAME OVER",True,Colors.white)
restart_messenge_surface = pygame.font.Font(None,30).render("Press R to restart",True,Colors.white)
score_rect = pygame.Rect(320,55,170,60)
next_rect = pygame.Rect(320,215,170,180)

#game screen size
screen = pygame.display.set_mode((500,620))

#game title
pygame.display.set_caption("Python Tetris")

#game time clock
clock = pygame.time.Clock()

#create game
game = Game()

#setting the block drop speed
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE,200)

#game loop
while True:
    for event in pygame.event.get():
        #quit and close the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #use asd and space on keyboard to control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_a and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_d and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_s and game.game_over == False:
                game.move_down()
                game.update_score(0,1)
            if event.key == pygame.K_SPACE and game.game_over == False:
                game.rotate()
        
        #move down the block in certain pace
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
    
    #draw game screen
    score_value_surface = title_font.render(str(game.score),True,Colors.white)
    screen.fill(Colors.dark_blue)
    screen.blit(score_surface,(365,20,50,50))
    screen.blit(next_surface,(375,180,50,50))
    if game.game_over == True:
        screen.blit(game_over_surface,(320,450,50,50))
        screen.blit(restart_messenge_surface,(320,550,50,50))
    pygame.draw.rect(screen,Colors.light_blue,score_rect,0,10)
    screen.blit(score_value_surface,score_value_surface.get_rect(centerx = score_rect.centerx,centery = score_rect.centery))
    pygame.draw.rect(screen,Colors.light_blue,next_rect,0,10)
    game.draw(screen)

    #update the game display screen
    pygame.display.update()

    #initialize game pace
    clock.tick(60)