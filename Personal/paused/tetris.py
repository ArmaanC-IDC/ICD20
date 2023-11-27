'''
1. init variables (screen, clock, 1 list for each block)
2. fill all the shapes with a color
3. init a rectangle for each square of a grid

start the while loop
create a random piece(.append a random inited list)
in the event loop:
    if arrow left, move left
    if arrow right, move right
    if down arrow, start a while it doesn't collide with anything (use code below)
        nested_list1 = [1, 2, 3]
        nested_list2 = ["Hello", "World", "!"]
        nested_list3 = [True, False, False, True]
        nested_list4 = [i for i in range(10, 20000, 2)]
        main_list = [nested_list1, nested_list2, nested_list3, nested_list4]

        for nested_list in main_list:
            for element in nested_list:
                print(element)

if a full rectangle is full (all grid rects in a a line are True, delete everything)
    '''

import pygame
from sys import exit
from random import randient
pygame.init()

class Z_piece:
    def __init__(self, color, x_pos, y_pos):
        self.color = color
        piece_top = pygame.surface.Surface((50, 25))
        piece_top_rect = piece_top.get_rect(topright = (x_pos, y_pos))
        piece_mid = pygame.surface.Surface((50, 25))
        piece_mid_rect = piece_mid.get_rect(topright = (x_pos + 25, y_pos + 25))
    
    def rotate():
        pass

    def delete_bottom():
        pass

