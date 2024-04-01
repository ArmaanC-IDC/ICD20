import pygame
import random
import time
pygame.init()

#10 X 10 grid
#init pygame screen
WIDTH,HEIGHT = 500,500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("MINESWEEPER")
font = pygame.font.Font(None,80)

#init game constants
MINE_COUNT = 15
MOVE_COOLDOWN = 10

#init game variables
game_state = 'running'

#get all mine coords
all_coords = [(x,y) for x in range(10) for y in range(10) if not (x <= 2 and y <= 2)]
mine_coords_list = random.sample(all_coords,k=MINE_COUNT)

#import images
mine_image = pygame.image.load("unit 5\minesweeper\mine.png")
mine_image = pygame.transform.scale(mine_image, (50,50))

#init grid variables
closed_coords = [(x,y) for x in range(10) for y in range(10) if (x,y)!=(0,0)]
open_coords = [(0,0)]


#init player move variables
player_coords = [0,0]
move_timer = MOVE_COOLDOWN

#define functions
#get_near_mine_count - loops through all tiles and assigns them a number (the number of mines next to them)
def get_near_mine_count():
    #get all grid spaces the number of mines next to them
    all_grid_spaces = [(x,y) for x in range(10) for y in range(10)]
    mine_count_list = []
    for el in all_grid_spaces:
        mine_count = 0
        coords_around = [(x,y) for x in range(el[0]-1,el[0]+2) for y in range(el[1]-1,el[1]+2) if (x,y)!= (el[0],el[1])]
        for around_coord in coords_around:
            if around_coord in mine_coords_list:
                mine_count +=1
        mine_count_list.append(mine_count)
    return mine_count_list, all_grid_spaces

#draw_grid - draws all grid spaces including open ones, changes color based on player coords, 
#puts the number of sorrounding mines on the grids
def draw_grid(player_coords, closed_coords, open_coords,mine_coords_list):
    for x,y in closed_coords:
        if (x+y)%2==0:
            if [x,y]==player_coords:
                pygame.draw.rect(screen,'lightgreen',pygame.Rect(x*50,y*50,50,50))
            else:
                pygame.draw.rect(screen,'chartreuse2',pygame.Rect(x*50,y*50,50,50))
        else:
            if [x,y]==player_coords:
                pygame.draw.rect(screen,'seagreen3',pygame.Rect(x*50,y*50,50,50))
            else:
                pygame.draw.rect(screen,'chartreuse4',pygame.Rect(x*50,y*50,50,50))
 
    for x,y in open_coords:
        if (x,y) in mine_coords_list:
            if (x+y)%2==0:
                if [x,y]==player_coords:
                    pygame.draw.rect(screen,'lightgreen',pygame.Rect(x*50,y*50,50,50))
                else:
                    pygame.draw.rect(screen,'chartreuse2',pygame.Rect(x*50,y*50,50,50))
            else:
                if [x,y]==player_coords:
                    pygame.draw.rect(screen,'seagreen3',pygame.Rect(x*50,y*50,50,50))
                else:
                    pygame.draw.rect(screen,'chartreuse4',pygame.Rect(x*50,y*50,50,50))
        else:
            if [x,y]==player_coords:
                pygame.draw.rect(screen,'seashell3',pygame.Rect(x*50,y*50,50,50))
            grid_space_number = all_grid_spaces.index((x,y))
            mine_number_text = font.render(str(mine_count_list[grid_space_number]),True,'BLACK')
            screen.blit(mine_number_text, (x*50,y*50))
            clear_adjacent_tiles(x,y)

#get_user_input - moves player_coords based on arrows, 
#if space is pressed puts the coord in open coord and removes from closed coords
def get_user_input(move_timer):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and move_timer<=0 and not player_coords[1] <=0:
        player_coords[1]-=1
        move_timer = MOVE_COOLDOWN
    if keys[pygame.K_DOWN] and move_timer<=0 and not player_coords[1] >=9:
        player_coords[1]+=1
        move_timer = MOVE_COOLDOWN
    if keys[pygame.K_RIGHT] and move_timer<=0 and not player_coords[0] >=9:
        player_coords[0]+=1
        move_timer = MOVE_COOLDOWN
    if keys[pygame.K_LEFT] and move_timer<=0 and not player_coords[0] <=0:
        player_coords[0]-=1
        move_timer = MOVE_COOLDOWN
    move_timer -=1

    if keys[pygame.K_SPACE]:
        try:
            closed_coords.remove((player_coords[0], player_coords[1]))
            open_coords.append((player_coords[0], player_coords[1]))
        except:
            pass

    return move_timer, player_coords, closed_coords, open_coords

def draw_mines(mine_coords_list, open_coords):
    game_state = 'running'
    mine_clicked = False
    for gone_coord in open_coords:
        for mine_coord in mine_coords_list:
            if mine_coord==gone_coord:
                mine_clicked = True
    
    if mine_clicked:
        for mine_coord in mine_coords_list:
            screen.blit(mine_image,(mine_coord[0]*50, mine_coord[1]*50))
        game_state = 'lost'
    return game_state

def clear_adjacent_tiles(x,y):
    sorrounding_coords = [(coordx,coordy) for coordx in range(x-1,x+2) for coordy in range (y-1,y+ 2) if (coordx,coordy)!=(x,y)]
    for coord in sorrounding_coords:
        if mine_count_list[all_grid_spaces.index((x,y))]==0:
            try:
                closed_coords.remove(coord)
                open_coords.append(coord)
            except:
                pass

def game_running(move_timer):
    #handle player inputs
    move_timer, player_coords, closed_coords, open_coords = get_user_input(move_timer)

    #draw grid
    draw_grid(player_coords, closed_coords, open_coords, mine_coords_list)

    #draw mines
    game_state = draw_mines(mine_coords_list, open_coords)
    return move_timer, game_state

mine_count_list, all_grid_spaces = get_near_mine_count()
running = True
while running:
    screen.fill('WHITE')
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False


    if game_state == 'running':
        move_timer, game_state = game_running(move_timer)
    move_timer, game_state = game_running(move_timer)
    
    pygame.time.Clock().tick(30)
    pygame.display.update()