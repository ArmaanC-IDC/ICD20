'''import pygame
from sys import exit
from random import randint
pygame.init() 

screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()

list = [pygame.surface.Surface((50,50)), pygame.surface.Surface((50,50))]
list[0].fill((255, 0, 0))
list[1].fill((0,255,0))

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(list[0], (100,100))
    screen.blit(list[1], (200,200))
    pygame.display.update()




nested_list1 = [1, 2, 3]
nested_list2 = ["Hello", "World", "!"]
nested_list3 = [True, False, False, True]
nested_list4 = [i for i in range(10, 20000, 2)]
main_list = [nested_list1, nested_list2, nested_list3, nested_list4]

for nested_list in main_list:
    for element in nested_list:
        print(element)'''

n = input("Enter a number")
print(n*)