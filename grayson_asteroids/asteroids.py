import pygame
import sys
import math
import random
import time

pygame.init()
HEIGHT = 800
WIDTH = 800
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
#Not greater than positive 180
angle = -90
fire_rate_counter = 0
center_screen_x = WIDTH//2
center_screen_y = HEIGHT//2
space_ship = pygame.transform.scale(space_ship,(25,25))
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
shoot_sound = pygame.mixer.Sound('grayson_asteroids/fire.wav')
asteroid_explode = pygame.mixer.Sound('grayson_asteroids/bangSmall.wav')
space_ship_explode = pygame.mixer.Sound('grayson_asteroids/bangLarge.wav')
invicible_timer = 180
invicible = False
invisable_count = 0
invisable = True
def detanate_asteroids(x_new,y_new,speed,size):
    x_speed = random.randint(-2,2)
    y_speed = random.randint(-2,2)
    for x in range(4):
        astroid_image = pygame.image.load('grayson_asteroids/Spaceship.png')
        astroid_image = pygame.transform.scale(astroid_image,(size,size))
        circle = {'rect': pygame.Rect(x_new, y_new, 2*size, 2*size), 'color': 'black', 'radius': size}
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
        print(asteroid_info)

def find_slope(p1,p2):
    largest = 1
    p1[1] = p1[1]*-1
    p2[1] = p2[1]*-1
    top = int(p2[1] - p1[1])
    bottom = int(p2[0] - p1[0])
    for i in range(top):
        if i != 0:
            if top / i == int and bottom / i == int and i != 0:
                largest = i
    top = top/largest
    bottom = bottom/largest
    return bottom, top
def move_asteroids():
    for aaa in range(len(asteroids)-1,-1,-1 ):
        asteroids[aaa][2] += asteroids[aaa][4]
        asteroids[aaa][3] += asteroids[aaa][5]
        asteroids[aaa][0] = {'rect': pygame.Rect(asteroids[aaa][2], asteroids[aaa][3], asteroids[aaa][8], asteroids[aaa][8]), 'color': 'black', 'radius': asteroids[aaa][8]}
        if asteroids[aaa][2] >= 850 or asteroids[aaa][2] <= -50 or asteroids[aaa][3] >= 850 or asteroids[aaa][3] <= -50:
            asteroids.remove(asteroids[aaa])
def move_bullets():
    for b in range(len(bullets)-1,-1,-1):
        try:
            bullets[b][0] = pygame.Rect(bullets[b][2],bullets[b][3],10,10)
            bullets[b][2] += bullets[b][4]
            bullets[b][3] += bullets[b][5]
            if bullets[b][2] >= 800 or bullets[b][2] <= 0 or bullets[b][3] >= 800 or bullets[b][3] <= 0:
                bullets.remove(bullets[b])
        except:
            pass
def add_meteor(speed,size,x,y):
    astroid_image = pygame.image.load('grayson_asteroids/Asteroid 1.png')
    astroid_image = pygame.transform.scale(astroid_image,(size,size))
    y_speed_meteor = speed
    x_speed_meteor =  0
    end_height = 810
    circle = {'rect': pygame.Rect(x, y, 2*size, 2*size), 'color': 'black', 'radius': size}
    asteroid_info = [circle,astroid_image,x,y,x_speed_meteor,y_speed_meteor,end_height,"h",size]
    asteroids.append(asteroid_info)
    
def add_asteroid(lowest,second_lowested,second_highest,highest,boo):
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
    circle = {'rect': pygame.Rect(x, y, 2*size, 2*size), 'color': 'black', 'radius': size}
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

def create_meteor_shower_line():
    num = WIDTH//100
    safe_area = random.randint(0,num - 3)
    safe_area = [safe_area, safe_area + 3]
    for count in range(5):
        for ast in range(0,safe_area[0]):
            add_meteor(2,100,ast*100,-10)
    for count in range(5):
        for ast in range(safe_area[1],num+1):
            add_meteor(2,100,ast*100,-10)

def create_bullet(x,y,ang,speed):
    ang += 90
    ang = math.radians(ang)
    x_speed = speed * (math.cos(ang))
    y_speed = speed * -1 *(math.sin(ang))
    bullet_image = pygame.image.load('grayson_asteroids/Bullet.png')
    bullet_image = pygame.transform.scale(bullet_image,(10,10))
    circle = pygame.Rect(x,y,10,10)
    bullet_info = [circle,bullet_image,x,y,x_speed,y_speed]
    bullets.append(bullet_info)
def create_bomb(x,y,speed,ang):
    ang += 90
    for b  in range(50):
        ang += 1
        x_speed = speed *math.cos(ang)
        y_speed = speed * -1 * (math.sin(ang))
        bullet_image = pygame.image.load('grayson_asteroids/Bullet.png')
        bullet_image = pygame.transform.scale(bullet_image,(10,10))
        circle = pygame.Rect(x,y,10,10)
        bullet_info = [circle,bullet_image,x,y,x_speed,y_speed]
        bullets.append(bullet_info)
def x_y_speeds(x,y,ang, speed):
    ang += 90
    image = pygame.transform.rotate(space_ship, -ang)
    rect = image.get_rect(center=(x, y))
    ang = math.radians(ang)
    x_speed = speed * (math.cos(ang))
    y_speed = speed * -1 *(math.sin(ang))
    return x_speed, y_speed, rect
while running:
    screen.fill('white')
    timer_1 = font.render(f"Time Before Asteroid Storm: {int(Storm_Timer)}", True, 'black')
    timer_2 = font.render(f"Time Before the Storm Ends: {int(active_timer)}", True, 'black')
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
            fire_rate_booster_count += 1
            bombs += 1
            asteroid_slow += 1
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
            fire_rate_booster_count += 1
            bombs += 1
            asteroid_slow += 1
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
            fire_rate_booster_count += 1
            bombs += 1
            asteroid_slow += 1
    fire_rate_boosters_left = font.render(f"Fire Rate Boosters Left: {int(fire_rate_booster_count)}",True,'black')
    bombs_left = font.render(f"Bombs Left: {int(bombs)}",True,'black')
    slows_left = font.render(f"Asteroids Slowers Left: {int(asteroid_slow)}",True,'black')
    lifes_lefts = font.render(f"Lifes Left: {int(lifes)}",True,'black')
    screen.blit(slows_left,(WIDTH-300,HEIGHT-50))
    screen.blit(lifes_lefts,(10,HEIGHT-50))
    screen.blit(bombs_left,(WIDTH-180,10))
    screen.blit(fire_rate_boosters_left,(10,10))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        x_speed, y_speed, center = x_y_speeds(player_x,player_x, angle, 3)
        player_x += x_speed
        player_y += y_speed
        if player_x <= 0:
            player_x = 0
        if player_x >= 775:
            player_x = 775
        if player_y >= 775:
            player_y = 775
        if player_y <= 0:
            player_y = 0
        screen.blit(pygame.transform.rotate(space_ship,angle),(player_x,player_y))
    if keys[pygame.K_s]:
        x_speed, y_speed, center = x_y_speeds(player_x,player_y,angle,3)
        player_x -= x_speed
        player_y -= y_speed
        if player_x <= 0:
            player_x = 0
        if player_x >= 775:
            player_x = 775
        if player_y >= 775:
            player_y = 775
        if player_y <= 0:
            player_y = 0
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
            create_bullet(player_x,player_y,angle,5)
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
            bc = 5
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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
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
                    print("Here")
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
                pygame.quit()
                sys.exit()
        else:
            invicible_timer -= 1
            if invicible_timer <= 0:
                invicible = False
            print(invicible)
    pygame.display.update()
    clock.tick(60)