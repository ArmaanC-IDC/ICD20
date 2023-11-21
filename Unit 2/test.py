'''n = int(input("how many numbers?: "))
strings_list = []
for i in range(n):
    strings_list.append(input(f"Enter string #{i+1}: "))
print(strings_list)

x = 5
y = 11
if x==5 and not y==10:
    print("x is 5")

x = [1,2,3,20]
print(sum(x))


a = 16
b = 17
if a==16 or not b==17:
    print("This works")
else:
    print("This doesn't")

x = 10
print(f"This works: {'Hi!':>{x}}")

list=[5,10,5]
print(sum(list))

x = " 1"
y = int(x)
print(y)

while True:
    while True:
        print("loop 2")
        break
    print("loop 1")
    break
print("done")'''

import pygame
from sys import exit
from random import randint
pygame.init()

screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()

pipe_low1 = pygame.Surface((50,400))
pipe_low1.fill((55,255,55))
pipe_low_rect1 = pipe_low1.get_rect(topright = (0, 400))

pipe_top1 = pygame.Surface((50,400))
pipe_top1.fill((55,255,55))
pipe_top_rect1 = pipe_top1.get_rect(bottomright = ((0, 0)))

height = randint(200,300)

pipe_low2 = pygame.Surface((50,400))
pipe_low2.fill((55,255,55))
pipe_low_rect2 = pipe_low2.get_rect(topright = (1800, height))

pipe_top2 = pygame.Surface((50,400))
pipe_top2.fill((55,255,55))
pipe_top_rect2 = pipe_top2.get_rect(bottomright = ((1800, height-200)))

player = pygame.Surface((50,50))
player.fill((0,0,0))
player_rect = player.get_rect(bottomleft = (50,50))
if player_rect.colliderect(pipe_top_rect1 or pipe_low_rect1 or pipe_top_rect2 or pipe_low_rect2):
    game_on = False