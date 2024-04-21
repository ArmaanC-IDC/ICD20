import pygame
import sys
import math
import random
import time

pygame.init()
#Create all variables
death_sound_check = True
HEIGHT = 800
WIDTH = 800
random_choice = None
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
running = True
asteroids = []
bullets = []
asteroid_locations = []
player_x = WIDTH//2
player_y = HEIGHT//2
counter = 0
c = 20
line_counter = 60
lifes = 3
bullet_counter = 0
bomb_counter =0
space_ship = pygame.image.load('grayson_asteroids/Spaceship.png')
background = pygame.image.load('grayson_asteroids/Background for game.png')
background = pygame.transform.scale(background,(900,900))
#Not greater than positive 180
angle = -90
fire_rate_counter = 0
center_screen_x = WIDTH//2
center_screen_y = HEIGHT//2
space_ship = pygame.transform.scale(space_ship,(30,30))
bombs = 3
slow_count = 0
fire_rate_booster_count = 3
fire_rate_boost = False
font = pygame.font.SysFont(None,36)
bc = 10
booster_delay = 0
Low = -4
Sec_Low = -2
Sec_High = 2
High = 4
slow = False
asteroid_slow = 3
Storm_Timer = 30
active_timer = 0
difficunity = 20
event_storm = random.randint(0,2)
death_sound = pygame.mixer.Sound('grayson_asteroids/Death Sound.wav')
shoot_sound = pygame.mixer.Sound('grayson_asteroids/fire.wav')
asteroid_explode = pygame.mixer.Sound('grayson_asteroids/bangSmall.wav')
space_ship_explode = pygame.mixer.Sound('grayson_asteroids/bangLarge.wav')
invicible_timer = 180
invicible = False
invisable_count = 0
invisable = True
first_lope = True
choice = 0 
difficunity_loop = True
Tutorial_step_1 = True
Tutorial_step_2 = False
Tutorial_step_3 = False
Tutorial_step_4 = False
Tutorial_step_5 = False
Tutorial_step_6 = False
Tutorial_step_7 = False
Tutorial_step_8 = False
Tutorial_step_9 = False
tutorial_counter = 0
player_choice = 0
score = 0
end_timer = 0
bullet_type = None
shooter_loop = True
burst_counter = 3
b_divide = 3
power_up_choice_loop = True
power_up_choice = None
speed_boosts = 3
mines = 3
bullet_mods = 3
decrease_difficulties = 3
spiral_bombs = 3
charged_bullets = 3
mines_list = []
player_speed = 3
bullet_mod_check = False
spiral_bomb_check = False
spiral_bomb_ang = 0
spiral_bomb_counter = 0
charged_bullets_check = False
charge_bullet_time_counter = 0
charge_bullet_counter =0
big_storm_check = True
#creates player bullets
def create_bullet(x,y,ang,speed,boo):
    #creates normal bullet
    if boo == False:
        ang += 90
        ang = math.radians(ang)
        x_speed = speed * (math.cos(ang))
        y_speed = speed * -1 *(math.sin(ang))
        bullet_image = pygame.image.load('grayson_asteroids/Good Bullet.png')
        bullet_image = pygame.transform.scale(bullet_image,(10,10))
        circle = pygame.Rect(x,y,10,10)
        bullet_info = [circle,bullet_image,x,y,x_speed,y_speed,boo,0]
        bullets.append(bullet_info)
    #creates charged bullet
    if boo == True:
        ang += 90
        ang = math.radians(ang)
        x_speed = speed * (math.cos(ang))
        y_speed = speed * -1 *(math.sin(ang))
        bullet_image = pygame.image.load('grayson_asteroids/Charged_bullet.png')
        bullet_image = pygame.transform.scale(bullet_image,(20,20))
        circle = pygame.Rect(x,y,10,10)
        bullet_info = [circle,bullet_image,x,y,x_speed,y_speed,boo,0]
        bullets.append(bullet_info) 
# blows up mines when they collide with other asteroids
def detanate_mine(x,y,boo):
    ang = 0
    ang += 90
    #Used for normal mines
    if boo == False:
        for b  in range(30):
            ang += 1
            x_speed = 2 *math.cos(ang)
            y_speed = 2 * -1 * (math.sin(ang))
            bullet_image = pygame.image.load('grayson_asteroids/Good Bullet.png')
            bullet_image = pygame.transform.scale(bullet_image,(10,10))
            circle = pygame.Rect(x,y,10,10)
            bullet_info = [circle,bullet_image,x,y,x_speed,y_speed,False,0]
            bullets.append(bullet_info)
    #used for exploding bullets
    elif boo == True:
        ang = 90
        for b in range(6):
            x_speed = 0.75 *math.cos(ang)
            y_speed = 0.75 * -1 * (math.sin(ang))
            bullet_image = pygame.image.load('grayson_asteroids/Good Bullet.png')
            bullet_image = pygame.transform.scale(bullet_image,(10,10))
            circle = pygame.Rect(x,y,10,10)
            bullet_info = [circle,bullet_image,x,y,x_speed,y_speed,False]
            bullets.append(bullet_info)
          
            ang += 45
def detanate_asteroids(x_new,y_new,speed,size):
    # Makes the asteroids explode when they are destroyed by bullets
    random_choice = random.randint(0,1)
    if random_choice == 0:
        x_speed = random.randint(-2,2)
        y_speed = random.randint(-2,2)
    else:
        y_speed = -1* random.randint(-2,2)
        x_speed = random.randint(-2,2)
    for x in range(4):
        astroid_image = pygame.image.load('grayson_asteroids/Asteroid 1.png')
        astroid_image = pygame.transform.scale(astroid_image,(size,size))
        circle = {'rect': pygame.Rect(x_new, y_new, size, size), 'color': 'black', 'radius': size}
        asteroid_info = [circle,astroid_image,x_new,y_new,x_speed,y_speed]
        if y_speed > 0:
            end_height = 800
            asteroid_info.append(end_height)
            asteroid_info.append("h")
        elif y_speed < 0:
            end_height = -10
            asteroid_info.append(end_height)
            asteroid_info.append("h")
        elif x_speed > 0:
            end_width = 800
            asteroid_info.append(end_width)
            asteroid_info.append("w")
        elif x_speed < 0:
            end_width = -10
            asteroid_info.append(end_width)
            asteroid_info.append("w")
        elif y_speed == 0 and x_speed > 0:
            end_width = 800
            asteroid_info.append(end_width)
            asteroid_info.append("w")
        elif y_speed == 0 and x_speed < 0:
            end_width = -10
            asteroid_info.append(end_width)
            asteroid_info.append("w")
        elif x_speed == 0 and y_speed > 0:
            end_height = 800
            asteroid_info.append(end_height)
            asteroid_info.append("h")
        elif x_speed == 0 and y_speed < 0:
            end_height = -10
            asteroid_info.append(end_height)
            asteroid_info.append("h")
        elif x_speed == 0 and y_speed == 0:
            x_speed = .1
            end_width = x_new + 18
            asteroid_info.append(end_width)
            asteroid_info.append("w")
        asteroid_info.append(size)
        asteroid_info.append(False)
        asteroids.append(asteroid_info)
        y_speed -= 1
        if y_speed <= 0:
            x_speed -= 1
def move_asteroids():
    #Moves all asteroids that are on the screen
    for aaa in range(len(asteroids)-1,-1,-1 ):
        asteroids[aaa][2] += asteroids[aaa][4]
        asteroids[aaa][3] += asteroids[aaa][5]
        asteroids[aaa][0] = {'rect': pygame.Rect(asteroids[aaa][2], asteroids[aaa][3], asteroids[aaa][8], asteroids[aaa][8]), 'color': 'black', 'radius': asteroids[aaa][8]}
        if asteroids[aaa][2] >= 850 or asteroids[aaa][2] <= -50 or asteroids[aaa][3] >= 850 or asteroids[aaa][3] <= -50:
            asteroids.remove(asteroids[aaa])
def move_bullets():
    #moves all bullets on the screen
    for b in range(len(bullets)-1,-1,-1):
     try:
        #Moves normal bullets
        if bullets[b][6] == False:
            try:
                bullets[b][0] = pygame.Rect(bullets[b][2],bullets[b][3],10,10)
                bullets[b][2] += bullets[b][4]
                bullets[b][3] += bullets[b][5]
                if bullets[b][2] >= 800 or bullets[b][2] <= 0 or bullets[b][3] >= 800 or bullets[b][3] <= 0:
                    bullets.remove(bullets[b])
            except:
                pass
        #Moves charged bullets
        elif bullets[b][6] == True:
                bullets[b][0] = pygame.Rect(bullets[b][2],bullets[b][3],10,10)
                bullets[b][2] += bullets[b][4]
                bullets[b][3] += bullets[b][5]
                if bullets[b][2] > 800:
                    bullets[b][2] = 1
                if bullets[b][2] < 0:
                    bullets[b][2] = 799
                if bullets[b][3] < 0:
                    bullets[b][3] = 799
                if bullets[b][3] > 800:
                    bullets[b][3] = 1
                if bullets[b][7] >= 600:
                    bullets.remove(bullets[b])
                bullets[b][7] += 1

     except:
         pass

def move_mines():
    #Moves all mines and exploding bullets
    for b in range(len(mines_list)-1,-1,-1):
        try:
            mines_list[b][0] = pygame.Rect(mines_list[b][2],mines_list[b][3],10,10)
            mines_list[b][2] += mines_list[b][4]
            mines_list[b][3] += mines_list[b][5]
            if mines_list[b][2] >= 800 or mines_list[b][2] <= 0 or mines_list[b][3] >= 800 or mines_list[b][3] <= 0:
                mines_list.remove(mines_list[b])
        except:
            pass

def add_meteor(speed,size,x,y):
    # Adds a meteor at the top of the screen that moves down and cannot be destroyed
    astroid_image = pygame.image.load('grayson_asteroids/Asteroid 1.png')
    astroid_image = pygame.transform.scale(astroid_image,(size,size))
    y_speed_meteor = speed
    x_speed_meteor =  0
    end_height = 810
    circle = {'rect': pygame.Rect(x, y, size, size), 'color': 'black', 'radius': size}
    asteroid_info = [circle,astroid_image,x,y,x_speed_meteor,y_speed_meteor,end_height,"h",size]
    asteroids.append(asteroid_info)
def add_asteroid(lowest,second_lowested,second_highest,highest,boo):
    # Adds asteroids and randomizes their movements
    size = random.randint(10,101)
    checker = random.randint(0,1)
    end_width = None
    if checker == 0:
        x = random.randint(-10,810)
        y = random.choice([HEIGHT+10,-10])
        if y == HEIGHT + 10:
            x_speed_asteroid = random.randint(second_lowested,second_highest)
            y_speed_asteroid = random.randint(lowest,second_lowested)
            end_height = 0
        else:
            x_speed_asteroid = random.randint(second_lowested,second_highest)
            y_speed_asteroid = random.randint(second_highest,highest)
            end_height = HEIGHT+10
    else:
        x = random.choice([-10,WIDTH+10])
        y = random.randint(-10,810)
        if x == -10:
            x_speed_asteroid = random.randint(second_highest,highest)
            y_speed_asteroid = random.randint(second_lowested,second_highest)
            end_height = WIDTH+10
        else:
            x_speed_asteroid = random.randint(lowest,second_lowested)
            y_speed_asteroid = random.randint(second_lowested,second_highest)
            end_width = -10
    astroid_image = pygame.image.load('grayson_asteroids/Asteroid 1.png')
    astroid_image = pygame.transform.scale(astroid_image,(size,size))
    circle = {'rect': pygame.Rect(x, y, size, size), 'color': 'black', 'radius': size}
    asteroid_info = [circle,astroid_image,x,y,x_speed_asteroid,y_speed_asteroid]
    if end_width != None:
        asteroid_info.append(end_width)
        asteroid_info.append("w")
    else: 
        asteroid_info.append(end_height)
        asteroid_info.append("h")
    asteroid_info.append(size)
    asteroid_info.append(boo)
    asteroids.append(asteroid_info)
def create_mine(x,y):
    # Creates six mines around the player
    ang = 0
    for m in range(6):
        x_speed = 0.75 *math.cos(ang)
        y_speed = 0.75 * -1 * (math.sin(ang))
        bullet_image = pygame.image.load('grayson_asteroids/Mine.png')
        bullet_image = pygame.transform.scale(bullet_image,(25,25))
        circle = pygame.Rect(x,y,10,10)
        bullet_info = [circle,bullet_image,x,y,x_speed,y_speed,False]
        mines_list.append(bullet_info)
        if ang >= 180:
            ang = -180
        if ang <= -180:
            ang = 180
        ang += 45
def create_explosive_bullet(x,y,ang):
    #creates a single mine that goes towards the player direction and looks like a bullet
    ang += 90
    ang = math.radians(ang)
    x_speed = 5 *math.cos(ang)
    y_speed = 5 * -1 * (math.sin(ang))
    bullet_image = pygame.image.load('grayson_asteroids/Good Bullet.png')
    bullet_image = pygame.transform.scale(bullet_image,(10,10))
    circle = pygame.Rect(x,y,10,10)
    bullet_info = [circle,bullet_image,x,y,x_speed,y_speed,True]
    mines_list.append(bullet_info)
def create_meteor_shower_line():
    #creates a line of indestructible meteors at the top of the screen
    num = WIDTH//100
    safe_area = random.randint(0,num - 3)
    safe_area = [safe_area, safe_area + 3]
    for count in range(5):
        for ast in range(0,safe_area[0]):
            add_meteor(2,100,ast*100,-10)
    for count in range(5):
        for ast in range(safe_area[1],num+1):
            add_meteor(2,100,ast*100,-10)


def create_bomb(x,y,speed,ang):
    #creates a ring of bullets around the player
    ang += 90
    for b  in range(50):
        ang += 1
        x_speed = speed *math.cos(ang)
        y_speed = speed * -1 * (math.sin(ang))
        bullet_image = pygame.image.load('grayson_asteroids/Good Bullet.png')
        bullet_image = pygame.transform.scale(bullet_image,(10,10))
        circle = pygame.Rect(x,y,10,10)
        bullet_info = [circle,bullet_image,x,y,x_speed,y_speed,False,0]
        bullets.append(bullet_info)
def x_y_speeds(x,y,ang, speed):
    #creates the speed of the player based off an angle
    ang += 90
    image = pygame.transform.rotate(space_ship, -ang)
    rect = image.get_rect(center=(x, y))
    ang = math.radians(ang)
    x_speed = speed * (math.cos(ang))
    y_speed = speed * -1 *(math.sin(ang))
    return x_speed, y_speed, rect
while running:
    #Fills the screen
    screen.blit(background,(0,0))
    if first_lope == True:
        #asks the player if the want to do the tutorial or the main game
        tutorial_text1 = font.render(f"Press 1 to continue to the main game.",True,'white')
        tutorial_text2 = font.render(f"Press 2 to continue to the tutorial", True, 'white')
        screen.blit(tutorial_text1,(150, HEIGHT// 2 -100))
        screen.blit(tutorial_text2,(150, HEIGHT// 2  + 100))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            choice = 1
            first_lope = False
        elif keys[pygame.K_2]:
            choice = 2
            first_lope = False
            lifes = 999
#MAIN GAME
    elif choice == 1:
        #Asks the player what difficunty they want to done
        difficunity_text1 = font.render(f"Press q to play on Easy Mode",True,'white')
        difficunity_text2 = font.render(f"Press w to play on Medium Mode",True,'white')
        difficunity_text3 = font.render(f"Press e to play on Hard Mode",True,'white')
        score_text = font.render(f"Your score is: {score}!",True,'white')
        if difficunity_loop == True:
            screen.blit(difficunity_text1,(100,HEIGHT- 700))
            screen.blit(difficunity_text2,(100,HEIGHT- 600))
            screen.blit(difficunity_text3,(100,HEIGHT- 500))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                c = 40
                difficunity = 40
                difficunity_loop = False
            if keys[pygame.K_w]:
                c = 30
                difficunity = 30
                difficunity_loop = False
            if keys[pygame.K_e]:
                c = 20
                difficunity = 20
                difficunity_loop = False

        if difficunity_loop == False:
            #asks the player want shoot they want
            if shooter_loop == True:
             shooter_option_1 = font.render(f"Press 1 to select classic shooter",True,'white')
             shooter_option_2 = font.render(f"Press 2 to select Shotgun shooter",True,'white')
             shooter_option_3 = font.render(f"Press 3 to select Burst shooter",True,'white')
             screen.blit(shooter_option_1,(WIDTH//2-100,HEIGHT//2 - 100))
             screen.blit(shooter_option_2,(WIDTH//2-100,HEIGHT//2 ))
             screen.blit(shooter_option_3,(WIDTH//2-100,HEIGHT//2 + 100))
             keys = pygame.key.get_pressed()
             if keys[pygame.K_1]:
                 bullet_type = 1
                 shooter_loop = False
                 bc = 10
             elif keys[pygame.K_2]:
                 bullet_type = 2
                 shooter_loop = False
                 bc = 25
             elif keys[pygame.K_3]:
                 bullet_type = 3
                 shooter_loop = False
                 bc = 40
            else:
             #asks the player want powerups they want
             if power_up_choice_loop == True:
                power_up_choices1 = font.render(f"Press Q to select Asteroid Slowers, bombs, fire rate booster", True, 'white')
                power_up_choices2 = font.render(f"Press W to select Speed Booster, Mines, Shooter Mod", True, 'white')
                power_up_choices3 = font.render(f"Press E to select Decrease Difficulty, Spiral Bombs, Charge Bullets", True, 'white')
                screen.blit(power_up_choices1,(10,50))
                screen.blit(power_up_choices2,(10,100))
                screen.blit(power_up_choices3,(10,150))
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:
                    power_up_choice = 1
                    power_up_choice_loop = False
                elif keys[pygame.K_w]:
                    power_up_choice = 2
                    power_up_choice_loop = False
                elif keys[pygame.K_e]:
                    power_up_choice = 3
                    power_up_choice_loop = False
             else:
                #Game begins
                screen.blit(background,(0,0))
                timer_1 = font.render(f"Time Before Asteroid Storm: {int(Storm_Timer)}", True, 'white')
                timer_2 = font.render(f"Time Before the Storm Ends: {int(active_timer)}", True, 'white')
                #Checks to see if there is time before the next storm
                if Storm_Timer > 0:
                    Storm_Timer -= clock.get_time() / 1000
                    screen.blit(timer_1, (WIDTH//2 - 150, 50))
                    if Storm_Timer <= 0:
                        if event_storm == 0:
                            active_timer = 15
                        if event_storm == 1:
                            active_timer = 10
                        if event_storm == 2:
                            active_timer = 30
                #If the active timer is greater than zero and the storm equals one it greatly increases spawn rate
                if active_timer > 0 and event_storm == 1:
                    c  = difficunity -10
                    if big_storm_check == True:
                        difficunity -= 10
                        big_storm_check =False
                    active_timer -= clock.get_time() /1000
                    screen.blit(timer_2, (WIDTH//2 - 150, 50))
                    if active_timer <= 0:
                        difficunity -= 2
                        difficunity += 10
                        c = difficunity
                        Storm_Timer = 30
                        mines += 1
                        lifes += 1
                        bombs += 1
                        fire_rate_booster_count += 1
                        asteroid_slow += 1
                        speed_boosts += 1
                        bullet_mods += 1
                        decrease_difficulties += 1
                        spiral_bombs += 1
                        charged_bullets += 1
                        event_storm = random.randint(0,2)
                        big_storm_check = True
                #If the active timer is greater than zero and the storm equals 0 it spawns lines of meteors at the top of the screen
                if active_timer > 0 and event_storm == 0:
                    active_timer -= clock.get_time() / 1000
                    screen.blit(timer_2,(WIDTH//2 - 150, 50))
                    line_counter+= 1
                    if line_counter >= 180:
                        create_meteor_shower_line()
                        line_counter = 0
                    if active_timer <= 0:
                        difficunity -= 2
                        c = difficunity
                        Storm_Timer = 30
                        mines += 1
                        lifes += 1
                        bombs += 1
                        fire_rate_booster_count += 1
                        asteroid_slow += 1
                        speed_boosts += 1
                        bullet_mods += 1
                        decrease_difficulties += 1
                        spiral_bombs += 1
                        charged_bullets += 1
                        event_storm = random.randint(0,2)
                #If the active timer is greater than zero and the storm equals two asteroids will randomly have the chance to explode
                if active_timer > 0 and event_storm == 2:
                    active_timer -= clock.get_time() / 1000
                    screen.blit(timer_2,(WIDTH//2 - 150, 50))
                    line_counter+= 1
                    if line_counter >= 30:
                        add_asteroid(-4,-2,2,4,True)
                        line_counter = 0
                    if active_timer <= 0:
                        difficunity -= 2
                        c = difficunity
                        Storm_Timer = 30
                        mines += 1
                        lifes += 1
                        bombs += 1
                        fire_rate_booster_count += 1
                        asteroid_slow += 1
                        speed_boosts += 1
                        bullet_mods += 1
                        decrease_difficulties += 1
                        spiral_bombs += 1
                        charged_bullets += 1
                        event_storm = random.randint(0,2)
                #creats all the text
                fire_rate_boosters_left = font.render(f"Fire Rate Boosters Left: {int(fire_rate_booster_count)}",True,'white')
                bombs_left = font.render(f"Bombs Left: {int(bombs)}",True,'white')
                slows_left = font.render(f"Asteroids Slowers Left: {int(asteroid_slow)}",True,'white')
                lifes_lefts = font.render(f"Lifes Left: {int(lifes)}",True,'white')
                mines_lefts = font.render(f"Mines Left: {int(mines)}",True,'white')
                speed_boosts_lefts = font.render(f"Speed Boosters Left: {int(speed_boosts)}",True,'white')
                charged_bullets_left = font.render(f"Charge Shots Left: {int(charged_bullets)}",True,'white')
                decrease_difficulties_left = font.render(f"Decrease Difficulties Left: {int(decrease_difficulties)}",True,'white')
                shooter_mods_lefts = font.render(f"Bullet Mods Left: {int(bullet_mods)}",True,'white')
                spiral_bombs_lefts = font.render(f"Spiral Bombs Left: {int(spiral_bombs)}",True,'white')
                screen.blit(lifes_lefts,(10,HEIGHT-50))
                keys = pygame.key.get_pressed()
                #Blits the main text displaying info
                if power_up_choice == 1:
                    screen.blit(slows_left,(WIDTH-300,HEIGHT-50))
                    screen.blit(bombs_left,(WIDTH-180,10))
                    screen.blit(fire_rate_boosters_left,(10,10))
                elif power_up_choice == 2:
                    screen.blit(speed_boosts_lefts,(WIDTH-300,HEIGHT-50))
                    screen.blit(mines_lefts,(WIDTH-180,10))
                    screen.blit(shooter_mods_lefts,(10,10))
                elif power_up_choice == 3:
                    screen.blit(decrease_difficulties_left,(WIDTH-400,HEIGHT-50))
                    screen.blit(spiral_bombs_lefts,(WIDTH-280,10))
                    screen.blit(charged_bullets_left,(10,10))
                #Causes actions and movements based on buttons pressed
                if keys[pygame.K_w]:
                    x_speed, y_speed, center = x_y_speeds(player_x,player_x, angle, player_speed)
                    player_x += x_speed
                    player_y += y_speed
                    if player_x <= 0:
                        player_x = WIDTH - 26
                    if player_x >= 775:
                        player_x = 1
                    if player_y >= 775:
                        player_y = 1
                    if player_y <= 0:
                        player_y = HEIGHT - 26
                    screen.blit(pygame.transform.rotate(space_ship,angle),(player_x,player_y))
                if keys[pygame.K_s]:
                    x_speed, y_speed, center = x_y_speeds(player_x,player_y,angle,player_speed)
                    player_x -= x_speed
                    player_y -= y_speed
                    if player_x <= 0:
                        player_x = WIDTH - 26
                    if player_x >= 775:
                        player_x = 1
                    if player_y >= 775:
                        player_y = 1
                    if player_y <= 0:
                        player_y = HEIGHT - 26
                    screen.blit(pygame.transform.rotate(space_ship,angle),(player_x,player_y))
                if keys[pygame.K_a]:
                    angle += 3
                    screen.blit(pygame.transform.rotate(space_ship,angle),(player_x,player_y))
                if keys[pygame.K_d]:
                    angle += -3
                    screen.blit(pygame.transform.rotate(space_ship,angle),(player_x,player_y))
                if keys[pygame.K_SPACE]:
                    bullet_counter += 1
                    if bullet_type == 1:
                        if bullet_counter >= bc and bullet_mod_check == False:
                            bullet_counter = 0
                            create_bullet(player_x,player_y,angle,5,False)
                            pygame.mixer.Sound.play(shoot_sound)
                        if bullet_counter >= bc and bullet_mod_check == True:
                            bullet_counter = 0
                            create_explosive_bullet(player_x,player_y,angle)
                            pygame.mixer.Sound.play(shoot_sound)
                    if bullet_type == 2:
                        if bullet_counter >= bc and bullet_mod_check == False:
                            bullet_counter = 0
                            create_bullet(player_x,player_y,angle,5,False) 
                            create_bullet(player_x,player_y,angle + 5,5,False) 
                            create_bullet(player_x,player_y,angle + 10,5,False) 
                            create_bullet(player_x,player_y,angle - 5,5,False) 
                            create_bullet(player_x,player_y,angle - 10,5,False) 
                            pygame.mixer.Sound.play(shoot_sound)
                        if bullet_counter >= bc and bullet_mod_check == True:
                            bullet_counter = 0
                            create_bullet(player_x,player_y,angle,5,False) 
                            create_bullet(player_x,player_y,angle + 5,5,False) 
                            create_bullet(player_x,player_y,angle + 10,5,False) 
                            create_bullet(player_x,player_y,angle - 5,5,False) 
                            create_bullet(player_x,player_y,angle - 10,5,False) 
                            create_bullet(player_x,player_y,angle + 15,5,False) 
                            create_bullet(player_x,player_y,angle + 20,5,False) 
                            create_bullet(player_x,player_y,angle - 15,5,False) 
                            create_bullet(player_x,player_y,angle - 20,5,False) 
                            if angle < 0:
                                new_angle = angle + 360
                            else:
                                new_angle = angle
                            create_bullet(player_x,player_y,angle + 180,5,False) 
                            create_bullet(player_x,player_y,angle + 180 + 5,5,False) 
                            create_bullet(player_x,player_y,angle + 180 + 10,5,False) 
                            create_bullet(player_x,player_y,angle + 180 - 5,5,False) 
                            create_bullet(player_x,player_y,angle + 180- 10,5,False) 
                            create_bullet(player_x,player_y,angle + 180 + 15,5,False) 
                            create_bullet(player_x,player_y,angle + 180 + 15,5,False) 
                            create_bullet(player_x,player_y,angle + 180 - 15,5,False) 
                            create_bullet(player_x,player_y,angle + 180- 20,5,False) 
                            pygame.mixer.Sound.play(shoot_sound)
                    if bullet_type == 3:
                        if bullet_counter >= bc and bullet_mod_check == False:
                            burst_counter += 1
                            if burst_counter % b_divide == 0:
                                create_bullet(player_x,player_y,angle,5,False)
                                pygame.mixer.Sound.play(shoot_sound)
                            if burst_counter >= 20:
                                burst_counter = 0
                                bullet_counter = 0
                        if bullet_counter >= bc and bullet_mod_check == True:
                            burst_counter += 1
                            create_bullet(player_x,player_y,angle - 30,5,False)
                            create_bullet(player_x,player_y,angle,5,False)
                            create_bullet(player_x,player_y, angle + 30,5,False)
                            pygame.mixer.Sound.play(shoot_sound)
                            if burst_counter == 40:
                                burst_counter = 0
                                bullet_counter = 0
                    if charged_bullets_check == True:
                        charge_bullet_counter += 1
                        charge_bullet_time_counter += 1
                        print(charge_bullet_time_counter)
                        if charge_bullet_counter >= 60:
                            create_bullet(player_x,player_y, angle,5,True)
                            charge_bullet_counter = 0
                            pygame.mixer.Sound.play(shoot_sound)
                        if charge_bullet_time_counter >= 600:
                            charged_bullets_check = False
                            charge_bullet_time_counter = 0
                        
                if keys[pygame.K_q]:
                    booster_delay += 1
                    if power_up_choice == 1:
                        if booster_delay >= 10 and bombs > 0:
                            create_bomb(player_x,player_y,5,angle)
                            booster_delay = 0
                            bombs -= 1
                            booster_delay = 0
                    elif power_up_choice == 2:
                        if booster_delay >= 10 and mines > 0:
                            create_mine(player_x,player_y)
                            booster_delay = 0
                            mines -= 1
                    elif power_up_choice == 3:
                        if booster_delay >= 10 and spiral_bombs > 0:
                            spiral_bomb_check = True
                            booster_delay = 0
                            spiral_bombs -= 1
    
                if keys[pygame.K_e]:
                    booster_delay += 1
                    if power_up_choice == 1:
                        if fire_rate_booster_count > 0 and booster_delay >= 10:
                            fire_rate_booster_count -= 1
                            fire_rate_boost = True
                            if bullet_type == 1:
                                bc = 2
                            elif bullet_type == 2:
                                bc = 10
                            elif bullet_type == 3:
                                bc = 10
                                b_divide = 1   
                            booster_delay = 0
                    if power_up_choice == 2:
                        if bullet_mods > 0 and booster_delay >= 10:
                            bullet_mods -= 1
                            bullet_mod_check = True
                            booster_delay = 0
                    if power_up_choice == 3:
                        if charged_bullets > 0 and booster_delay >= 10:
                            charged_bullets -= 1
                            charged_bullets_check = True
                            booster_delay = 0
                if keys[pygame.K_LSHIFT]:
                    booster_delay += 1
                    if power_up_choice == 1:
                        if asteroid_slow > 0 and booster_delay >= 10:
                            asteroid_slow -= 1
                            High = 1
                            Sec_High = 1
                            Sec_Low = -1
                            Low = -1
                            slow = True
                            booster_delay = 0
                    if power_up_choice == 2:
                        if speed_boosts > 0 and booster_delay >= 10:
                            speed_boosts -= 1
                            slow = True
                            player_speed = 6
                            booster_delay = 0
                    if power_up_choice == 3:
                        if decrease_difficulties > 0 and booster_delay >= 10:
                            decrease_difficulties -= 1
                            difficunity += 2
                if bullet_mod_check == True:
                    fire_rate_booster_count += 1
                    if fire_rate_booster_count >= 600:
                        fire_rate_booster_count = 0
                        bullet_mod_check = False
                if slow == True:
                    slow_count += 1
                    if slow_count == 600:
                        High = 4
                        Sec_High = 2
                        Sec_Low = -2
                        Low = -4
                if slow == True:
                    slow_count += 1
                    if slow_count == 600:
                        player_speed = 3
                if fire_rate_boost == True:
                    fire_rate_counter += 1
                    if fire_rate_counter == 600:
                        if bullet_type == 1:
                            bc = 10
                            fire_rate_counter = 0
                            fire_rate_boost = False
                        if bullet_type == 2:
                            bc = 25
                            fire_rate_counter = 0
                            fire_rate_boost = False
                        if bullet_type == 3:
                            bc = 40
                            b_divide = 2
                            fire_rate_counter = 0
                            fire_rate_boost = False
                if spiral_bomb_check == True:
                    spiral_bomb_counter += 1
                    spiral_bomb_ang += 3
                    create_bullet(player_x,player_y,spiral_bomb_ang,5,False)
                    create_bullet(player_x,player_y,spiral_bomb_ang+180,5,False)
                    if spiral_bomb_counter >= 120:
                        spiral_bomb_check = False
                        spiral_bomb_counter = 0
                #blits the player at their location
                screen.blit(pygame.transform.rotate(space_ship,angle),(player_x,player_y))
                center = [player_x, player_y + 25]
                #moves all of the objects on the screen
                move_bullets()
                move_asteroids()
                move_mines()
                #Sets the spawnrate for the asteroids and spawns the asteroids
                counter += 1
                c = difficunity
                if counter >= c:
                    add_asteroid(Low,Sec_Low,Sec_High,High,False)
                    counter = 0
                #Blits all objects on the screen other than the player
                for b in range(0,len(bullets)):
                    screen.blit(bullets[b][1],(bullets[b][2],bullets[b][3]))
                for a in range(0,len(asteroids)):
                    screen.blit(asteroids[a][1],(asteroids[a][2],asteroids[a][3]))
                for cc in range(0,len(mines_list)):
                    screen.blit(mines_list[cc][1],(mines_list[cc][2],mines_list[cc][3]))
                #creates the player's hitbox
                hit_box = pygame.Rect(player_x,player_y,25,25)
                #Resets angle so it never is higher or lower than 180 or -180
                '''if angle > 180:
                    angle = -180
                if angle < -180:
                    angle = 180'''
                #checks for collisions with asteroids in bullets
                for b in range(len(bullets)-1,-1,-1):
                 if bullets[b][6] == False:
                    try:
                        for a in range(len(asteroids)-1,-1,-1):
                            if bullets[b][0].colliderect(asteroids[a][0]['rect']):
                                bullets.remove(bullets[b])
                                #checks to see if the asteroid explodes
                                if asteroids[a][9] == True:
                                    detanate_asteroids(asteroids[a][2],asteroids[a][3],2,20)
                                    asteroids.remove(asteroids[a])
                                    score += 100
                                    pygame.mixer.Sound.play(asteroid_explode)
                                else:
                                    #removes the asteroid from the game
                                    asteroids.remove(asteroids[a])
                                    pygame.mixer.Sound.play(asteroid_explode)
                                    score += 100
                    except:
                        pass
                 elif bullets[b][6] == True:
                    #same logic but for charged bullets that are not destroyed when they collide
                    try:
                        for a in range(len(asteroids)-1,-1,-1):
                            if bullets[b][0].colliderect(asteroids[a][0]['rect']):
                                if asteroids[a][9] == True:
                                    detanate_asteroids(asteroids[a][2],asteroids[a][3],2,20)
                                    asteroids.remove(asteroids[a])
                                    score += 100
                                else:
                                    asteroids.remove(asteroids[a])
                                    pygame.mixer.Sound.play(asteroid_explode)
                                score += 100
                    except:
                        pass
                for m in range(len(mines_list)-1,-1,-1):
                 #Moves and blows up mines
                 try:
                    for a in range(len(asteroids)-1,-1,-1):
                        if mines_list[m][0].colliderect(asteroids[a][0]['rect']):
                            detanate_mine(mines_list[m][2],mines_list[m][3],mines_list[m][6])
                            mines_list.remove(mines_list[m])
                            if asteroids[a][9] == True:
                                detanate_asteroids(asteroids[a][2],asteroids[a][3],2,20)
                                asteroids.remove(asteroids[a])
                                score += 100
                            else:
                                asteroids.remove(asteroids[a])
                                pygame.mixer.Sound.play(asteroid_explode)
                            score += 100
                 except:
                    pass   
                for a in range(len(asteroids)-1,-1,-1):
                    #Checks for player collision with asteroids
                    if hit_box.colliderect(asteroids[a][0]['rect']) and invicible == False:
                        lifes -= 1
                        asteroids.remove(asteroids[a])
                        pygame.mixer.Sound.play(space_ship_explode)
                        invicible = True
                        invicible_timer = 3000
                        if lifes == 0:
                            choice = 3
                    else:
                        invicible_timer -= 1
                        if invicible_timer <= 0:
                            invicible = False
                score += 1


#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    #Same logic as game above, however 999 lifes and acts as a tutorial
    elif choice == 2:
        Tutorial_step_1_text = font.render("Press A and D to rotate the Spaceship",True,'white')
        Tutorial_step_2_text = font.render("Press W and S to Move the the Spaceship Foward and Backward",True,'white')
        Tutorial_step_3_text = font.render("Press Q to spawn a bomb around your space ship",True,'white')
        Tutorial_step_4_text = font.render("Press E to greatly increase your fire rate",True,'white')
        Tutorial_step_5_text = font.render("Press Left Shift to slow any new asteroids",True,'white')
        Tutorial_step_6_text = font.render("If you get hit you will be invicible for 5 seconds",True,'white')
        Tutorial_step_7a_text = font.render("Every 30 seconds a random diaster will happen:",True,'white')
        Tutorial_step_7b_text = font.render("1) The spawn rate of asteroids will increase",True,'white')
        Tutorial_step_7c_text = font.render("2) Lines of armored asteroids will spawn at the top of the screen",True,'white')
        Tutorial_step_7d_text = font.render("3) Random destroyed asteroids will explode into smaller asteroids",True,'white')
        Tutorial_step_8_text = font.render("Every time you survive a disaster you get +1 of every powerup",True,'white')
        Tutorial_step_9_text = font.render("You've complete the tutorial! Congratulations!",True,'white')
        timer_1 = font.render(f"Time Before Asteroid Storm: {int(Storm_Timer)}", True, 'white')
        timer_2 = font.render(f"Time Before the Storm Ends: {int(active_timer)}", True, 'white')
        if Storm_Timer > 0:
            Storm_Timer -= clock.get_time() / 1000
            screen.blit(timer_1, (WIDTH//2 - 150, 50))
            if Storm_Timer <= 0:
                if event_storm == 0:
                    active_timer = 15
                if event_storm == 1:
                    active_timer = 10
                if event_storm == 2:
                    active_timer = 30
        if active_timer > 0 and event_storm == 1:
            c  = difficunity -15
            active_timer -= clock.get_time() /1000
            screen.blit(timer_2, (WIDTH//2 - 150, 50))
            if active_timer <= 0:
                difficunity -= 2
                c = difficunity
                Storm_Timer = 30
                mines += 1
                lifes += 1
                bombs += 1
                fire_rate_booster_count += 1
                asteroid_slow += 1
                speed_boosts += 1
                bullet_mods += 1
                decrease_difficulties += 1
                spiral_bombs += 1
                charged_bullets += 1
        if active_timer > 0 and event_storm == 0:
            active_timer -= clock.get_time() / 1000
            screen.blit(timer_2,(WIDTH//2 - 150, 50))
            line_counter+= 1
            if line_counter >= 180:
                create_meteor_shower_line()
                line_counter = 0
            if active_timer <= 0:
                difficunity -= 2
                c = difficunity
                Storm_Timer = 30
                mines += 1
                lifes += 1
                bombs += 1
                fire_rate_booster_count += 1
                asteroid_slow += 1
                speed_boosts += 1
                bullet_mods += 1
                decrease_difficulties += 1
                spiral_bombs += 1
                charged_bullets += 1
        if active_timer > 0 and event_storm == 2:
            active_timer -= clock.get_time() / 1000
            screen.blit(timer_2,(WIDTH//2 - 150, 50))
            line_counter+= 1
            if line_counter >= 30:
                add_asteroid(-4,-2,2,4,True)
                line_counter = 0
            if active_timer <= 0:
                difficunity -= 2
                c = difficunity
                Storm_Timer = 30
                mines += 1
                lifes += 1
                bombs += 1
                fire_rate_booster_count += 1
                asteroid_slow += 1
                speed_boosts += 1
                bullet_mods += 1
                decrease_difficulties += 1
                spiral_bombs += 1
                charged_bullets += 1
        fire_rate_boosters_left = font.render(f"Fire Rate Boosters Left: {int(fire_rate_booster_count)}",True,'white')
        bombs_left = font.render(f"Bombs Left: {int(bombs)}",True,'white')
        slows_left = font.render(f"Asteroids Slowers Left: {int(asteroid_slow)}",True,'white')
        lifes_lefts = font.render(f"Lifes Left: {int(lifes)}",True,'white')
        screen.blit(slows_left,(WIDTH-300,HEIGHT-50))
        screen.blit(lifes_lefts,(10,HEIGHT-50))
        screen.blit(bombs_left,(WIDTH-180,10))
        screen.blit(fire_rate_boosters_left,(10,10))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            x_speed, y_speed, center = x_y_speeds(player_x,player_x, angle, player_speed)
            player_x += x_speed
            player_y += y_speed
            if player_x <= 0:
                player_x = WIDTH - 25
            if player_x >= 775:
                player_x = 0
            if player_y >= 775:
                player_y = 0
            if player_y <= 0:
                player_y = HEIGHT - 25
            screen.blit(pygame.transform.rotate(space_ship,angle),(player_x,player_y))
        if keys[pygame.K_s]:
            x_speed, y_speed, center = x_y_speeds(player_x,player_y,angle,player_speed)
            player_x -= x_speed
            player_y -= y_speed
            if player_x <= 0:
                player_x = 0 + WIDTH
            if player_x >= 775:
                player_x = 775 - WIDTH
            if player_y >= 775:
                player_y = 775 - HEIGHT
            if player_y <= 0:
                player_y = 0 + HEIGHT
            screen.blit(pygame.transform.rotate(space_ship,angle),(player_x,player_y))
        if keys[pygame.K_a]:
            angle += 3
            screen.blit(pygame.transform.rotate(space_ship,angle),(player_x,player_y))
        if keys[pygame.K_d]:
            angle += -3
            screen.blit(pygame.transform.rotate(space_ship,angle),(player_x,player_y))
        if keys[pygame.K_SPACE]:
            bullet_counter += 1
            if bullet_counter >= bc:
                bullet_counter = 0
                create_bullet(player_x,player_y,angle,5,False)
                pygame.mixer.Sound.play(shoot_sound)

        if keys[pygame.K_q]:
            booster_delay += 1
            if booster_delay >= 10 and bombs > 0:
                create_bomb(player_x,player_y,5,angle)
                booster_delay = 0
                bombs -= 1
                booster_delay = 0
        if keys[pygame.K_e]:
            booster_delay += 1
            if fire_rate_booster_count > 0 and booster_delay >= 10:
                fire_rate_booster_count -= 1
                fire_rate_boost = True
                bc = 2
                booster_delay = 0
        if keys[pygame.K_LSHIFT]:
            booster_delay += 1
            if asteroid_slow > 0 and booster_delay >= 10:
                asteroid_slow -= 1
                High = 1
                Sec_High = 1
                Sec_Low = -1
                Low = -1
                slow = True
                booster_delay = 0
        if slow == True:
            slow_count += 1
            if slow_count == 600:
                High = 4
                Sec_High = 2
                Sec_Low = -2
                Low = -4
        if fire_rate_boost == True:
            fire_rate_counter += 1
            if fire_rate_counter == 600:
                bc = 10
                fire_rate_counter = 0
                fire_rate_boost = False
        screen.blit(pygame.transform.rotate(space_ship,angle),(player_x,player_y))
        center = [player_x, player_y + 25]
        move_bullets()
        move_asteroids()
        counter += 1
        if counter >= c:
            add_asteroid(Low,Sec_Low,Sec_High,High,False)
            counter = 0
        for b in range(0,len(bullets)):
            screen.blit(bullets[b][1],(bullets[b][2],bullets[b][3]))
        for a in range(0,len(asteroids)):
            screen.blit(asteroids[a][1],(asteroids[a][2],asteroids[a][3]))
        hit_box = pygame.Rect(player_x,player_y,25,25)
        if angle > 180:
            angle = -180
        if angle < -180:
            angle = 180
        x = len(bullets)-1
        for b in range(x,-1,-1):
         try:
            for a in range(len(asteroids)-1,-1,-1):
                if bullets[b][0].colliderect(asteroids[a][0]['rect']):
                    bullets.remove(bullets[b])
                    if asteroids[a][9] == True:
                        detanate_asteroids(asteroids[a][2],asteroids[a][3],2,20)
                        asteroids.remove(asteroids[a])
                    else:
                        asteroids.remove(asteroids[a])
                        pygame.mixer.Sound.play(asteroid_explode)
         except:
            pass
            
        for a in range(len(asteroids)-1,-1,-1):
            if hit_box.colliderect(asteroids[a][0]['rect']) and invicible == False:
                lifes -= 1
                asteroids.remove(asteroids[a])
                pygame.mixer.Sound.play(space_ship_explode)
                invicible = True
                invicible_timer = 3000
                if lifes == 0:
                    pygame.mixer.Sound.play(death_sound)
                    pygame.quit()
                    sys.exit()
            else:
                invicible_timer -= 1
                if invicible_timer <= 0:
                    invicible = False

        if Tutorial_step_1 == True:
            screen.blit(Tutorial_step_1_text,(WIDTH-600,HEIGHT-600))
            tutorial_counter += 1
            if tutorial_counter >= 300:
                tutorial_counter = 0
                Tutorial_step_1 = False
                Tutorial_step_2 = True
        if Tutorial_step_2 == True:
            screen.blit(Tutorial_step_2_text,(WIDTH-775,HEIGHT-600))
            tutorial_counter += 1
            if tutorial_counter >= 300:
                tutorial_counter = 0
                Tutorial_step_2 = False
                Tutorial_step_3 = True
        if Tutorial_step_3 == True:
            screen.blit(Tutorial_step_3_text,(WIDTH-700,HEIGHT-600))
            tutorial_counter += 1
            if tutorial_counter >= 300:
                tutorial_counter = 0
                Tutorial_step_3 = False
                Tutorial_step_4 = True
        if Tutorial_step_4 == True:
            screen.blit(Tutorial_step_4_text,(WIDTH-600,HEIGHT-600))
            tutorial_counter += 1
            if tutorial_counter >= 300:
                tutorial_counter = 0
                Tutorial_step_4 = False
                Tutorial_step_5 = True
        if Tutorial_step_5 == True:
            screen.blit(Tutorial_step_5_text,(WIDTH-600,HEIGHT-600))
            tutorial_counter += 1
            if tutorial_counter >= 300:
                tutorial_counter = 0
                Tutorial_step_5 = False
                Tutorial_step_6 = True
        if Tutorial_step_6 == True:
            screen.blit(Tutorial_step_6_text,(WIDTH-600,HEIGHT-600))
            tutorial_counter += 1
            if tutorial_counter >= 300:
                tutorial_counter = 0
                Tutorial_step_6 = False
                Tutorial_step_7 = True
        if Tutorial_step_7 == True:
            screen.blit(Tutorial_step_7a_text,(WIDTH-790,HEIGHT-600))
            screen.blit(Tutorial_step_7b_text,(WIDTH-790,HEIGHT-550))
            screen.blit(Tutorial_step_7c_text,(WIDTH-790,HEIGHT-500))
            screen.blit(Tutorial_step_7d_text,(WIDTH-790,HEIGHT-450))
            tutorial_counter += 1
            if tutorial_counter >= 600:
                tutorial_counter = 0
                Tutorial_step_7 = False
                Tutorial_step_8 = True
        if Tutorial_step_8 == True:
            screen.blit(Tutorial_step_8_text,(WIDTH-750,HEIGHT-600))
            tutorial_counter += 1
            if tutorial_counter >= 300:
                tutorial_counter = 0
                Tutorial_step_8 = False
                Tutorial_step_9 = True
        if Tutorial_step_9 == True:
            screen.blit(Tutorial_step_9_text,(WIDTH-750,HEIGHT-600))
            tutorial_counter += 1
            if tutorial_counter >= 300:
                tutorial_counter = 0
                Tutorial_step_9 = False
    if choice == 3:
        if death_sound_check == True:
            pygame.mixer.Sound.play(death_sound)
            death_sound_check = False
        screen.blit(score_text,(WIDTH//2 - 150,HEIGHT//2 - 50))
        end_timer += 1
        if end_timer >= 600:
            pygame.quit()
            sys.exit()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.Sound.play(death_sound)
                pygame.quit()
                sys.exit()
    pygame.display.update()
    clock.tick(60)