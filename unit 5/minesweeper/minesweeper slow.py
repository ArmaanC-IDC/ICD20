import pygame
import random
import time
pygame.init()
pygame.mixer.init()

#CHANGES TO ADD
#DIFFICULTY LEVELS (5X5 grid, 10X10, 15X15)


#init pygame screen
WIDTH,HEIGHT = 500,500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("MINESWEEPER")
font = pygame.font.Font(None,80)
font2 = pygame.font.Font(None,40)
clock = pygame.time.Clock()

#init game constants
MOVE_COOLDOWN = 3

#init game variables
game_state = 'running'

#import images
mine_image = pygame.image.load("unit 5\minesweeper\mine.png")
mine_image = pygame.transform.scale(mine_image, (50,50))

flag_image = pygame.image.load("grayson_asteroids/Asteroid 1.png")
flag_image = pygame.transform.scale(flag_image,(50,50))

#import sounds
game_loose_sound = pygame.mixer.Sound('unit 5\minesweeper\game_lose.wav')
game_win_sound = pygame.mixer.Sound('unit 5\minesweeper\game_win.mp3')
background_music = pygame.mixer.music.load('unit 5/minesweeper/background_music.mp3')
pygame.mixer.music.set_volume(0.05)



def start_game():
    grid_size, mine_count = get_difficulty_level()

    #get all mine coords
    all_coords = [(x,y) for x in range(grid_size) for y in range(grid_size) if not (x <= 2 and y <= 2)]
    mine_coords_list = random.sample(all_coords,k=mine_count)

    closed_coords = [(x,y) for x in range(grid_size) for y in range(grid_size) if (x,y)!=(0,0)]
    open_coords = [(0,0)]
    #init flagging variables
    flagged_coords = []
    #init player move variables
    player_coords = [0,0]
    move_timer = MOVE_COOLDOWN
    unchecked_coords = open_coords
    return closed_coords, open_coords, flagged_coords, player_coords, move_timer, grid_size, mine_coords_list, unchecked_coords

def get_difficulty_level():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running = False
        screen.fill('WHITE')
        pygame.draw.rect(screen,'GREEN',pygame.Rect(50,250,100,100))
        pygame.draw.rect(screen,'YELLOW',pygame.Rect(200,250,100,100))
        pygame.draw.rect(screen,'RED',pygame.Rect(350,250,100,100))
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        #easy mode
        if pygame.Rect(50,250,100,100).collidepoint(mouse_pos) and mouse_click[0]:
            grid_size = 7
            mine_count = 14
            running = False

        #medium
        elif pygame.Rect(200,250,100,100).collidepoint(mouse_pos) and mouse_click[0]:
            grid_size = 10
            mine_count = 20
            running = False

        #hard
        elif pygame.Rect(350,250,100,100).collidepoint(mouse_pos) and mouse_click[0]:
            grid_size = 15
            mine_count = 15
            running = False
        pygame.display.update()
    return grid_size, mine_count

        

#define functions
def add_color_nums():
    for x,y in open_coords:
        grid_space_number = all_grid_spaces.index((x,y))
        num_of_mines = mine_count_list[grid_space_number]
        not_zero = True
        if num_of_mines==1:
            mine_number_text = font.render(str(num_of_mines),True,'CADETBLUE3')
        elif num_of_mines==2:
            mine_number_text = font.render(str(num_of_mines),True,'DARKGREEN')
        elif num_of_mines==3:
            mine_number_text = font.render(str(num_of_mines),True,'CRIMSON')
        elif num_of_mines==4:
            mine_number_text = font.render(str(num_of_mines),True,'DARKBLUE')
        elif num_of_mines==5:
            mine_number_text = font.render(str(num_of_mines),True,'BROWN4')
        elif num_of_mines==6:
            mine_number_text = font.render(str(num_of_mines),True,'CYAN')
        elif num_of_mines==7:
            mine_number_text = font.render(str(num_of_mines),True,'BLACK')
        elif num_of_mines==8:
            mine_number_text = font.render(str(num_of_mines),True,'GRAY')
        else:
            not_zero = False
        if not_zero:
            screen.blit(mine_number_text, (x*50,y*50))

        if (x,y) in mine_coords_list:
            if (x+y)%2==0:
                pygame.draw.rect(screen,'chartreuse2',pygame.Rect(x*50,y*50,50,50))
            else:
                pygame.draw.rect(screen,'chartreuse4',pygame.Rect(x*50,y*50,50,50))

#get_near_mine_count - loops through all tiles and assigns them a number (the number of mines next to them)
def get_near_mine_count():
    #get all grid spaces the number of mines next to them
    all_grid_spaces = [(x,y) for x in range(grid_size) for y in range(grid_size)]
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
        if (x,y) not in mine_coords_list:
            if [x,y]==player_coords:
                pygame.draw.rect(screen,'seashell3',pygame.Rect(x*50,y*50,50,50))

            add_color_nums()
            clear_adjacent_tiles(x,y)
    
    for x,y in flagged_coords:
        screen.blit(flag_image,(x*50,y*50))

#get_user_input - moves player_coords based on arrows, 
#if space is pressed puts the coord in open coord and removes from closed coords
def get_user_input(move_timer):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and move_timer<=0 and not player_coords[1] <=0:
        player_coords[1]-=1
        move_timer = MOVE_COOLDOWN
    if keys[pygame.K_DOWN] and move_timer<=0 and not player_coords[1] >=grid_size-1:
        player_coords[1]+=1
        move_timer = MOVE_COOLDOWN
    if keys[pygame.K_RIGHT] and move_timer<=0 and not player_coords[0] >=grid_size-1:
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
    
    if keys[pygame.K_LSHIFT]:
        flagged_coords.append((player_coords[0], player_coords[1]))

    if keys[pygame.K_RSHIFT]:
        try:
            flagged_coords.remove((player_coords[0],player_coords[1]))
        except:
            pass
    return move_timer, player_coords, closed_coords, open_coords

#draw_mines - loops through all open tiles and sets game state to lost if a mine is open,
#draws all mines if game is lost
def game_state_control(mine_coords_list, open_coords):
    game_state = 'running'

    #check if a mine is on an open tilec
    for gone_coord in open_coords:
        if gone_coord in mine_coords_list:
            game_state = 'lost'
            pygame.mixer.Sound.play(game_loose_sound)

    if len(closed_coords)==len(mine_coords_list):
        game_state = 'won'
        pygame.mixer.Sound.play(game_win_sound)
    return game_state

#clear all tiles around an x and y coord (my grid coord not pygame coords)
def clear_adjacent_tiles(x,y):
    sorrounding_coords = [(coordx,coordy) for coordx in range(x-1,x+2) for coordy in range (y-1,y+ 2) if (coordx,coordy)!=(x,y)]
    if mine_count_list[all_grid_spaces.index((x,y))]==0:
        for coord in sorrounding_coords:
            try:
                closed_coords.remove(coord)
                open_coords.append(coord)
            except:
                pass
    else:
        for coord in sorrounding_coords:
            try:
                if mine_count_list[all_grid_spaces.index((coord))]==0 and coord not in mine_coords_list:
                    try:
                        closed_coords.remove(coord)
                        open_coords.append(coord)
                    except:
                        pass
            except:
                pass

#calls get_user_input(), draw_grid(), and draw_mines()
def game_running(move_timer):
    
    #handle player inputs
    move_timer, player_coords, closed_coords, open_coords = get_user_input(move_timer)

    
    #draw grid
    draw_grid(player_coords, closed_coords, open_coords, mine_coords_list)

    #draw mines
    game_state = game_state_control(mine_coords_list, open_coords)
    return move_timer, game_state

#handles everything that happens once the game is lost
def game_loose():    
    pygame.mixer.music.stop()
    for x,y in closed_coords:
        if (x+y)%2==0:
            pygame.draw.rect(screen,'chartreuse2',pygame.Rect(x*50,y*50,50,50))
        else:
            pygame.draw.rect(screen,'chartreuse4',pygame.Rect(x*50,y*50,50,50))

    add_color_nums()
    
    #display all mines
    for mine_coord in mine_coords_list:
        screen.blit(mine_image,(mine_coord[0]*50, mine_coord[1]*50))
    
#handles everything that happens once the game is won
def game_won():
    pygame.mixer.music.stop()
    for x,y in closed_coords:
        if (x+y)%2==0:
            pygame.draw.rect(screen,'chartreuse2',pygame.Rect(x*50,y*50,50,50))
        else:
            pygame.draw.rect(screen,'chartreuse4',pygame.Rect(x*50,y*50,50,50))

    add_color_nums()
    
    #display all mines
    for mine_coord in mine_coords_list:
        screen.blit(mine_image,(mine_coord[0]*50, mine_coord[1]*50))
    
pygame.mixer.music.play(-1)

closed_coords, open_coords, flagged_coords, player_coords, move_timer, grid_size, mine_coords_list, unchecked_coords = start_game()
screen = pygame.display.set_mode((grid_size*50,grid_size*50))
mine_count_list, all_grid_spaces = get_near_mine_count()
running = True
while running:
    screen.fill('WHITE')
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False



    if game_state == 'running':
        move_timer, game_state = game_running(move_timer)
    elif game_state=='lost':
        game_loose()
    elif game_state=='won':
        game_won()

    print(clock.get_fps())
    for mine_coord in mine_coords_list:
        screen.blit(mine_image,(mine_coord[0]*50, mine_coord[1]*50))
    
    

    
    clock.tick(30)
    pygame.display.update()