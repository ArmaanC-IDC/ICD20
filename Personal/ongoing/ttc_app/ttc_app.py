#6 screens. 
import pygame as pg
import sys
pg.init()

file = open("Personal/ongoing/ttc_app/data.txt", 'a')
file.write("data1 \n")
file.write("data2 \n")
file.close()

file1 = open("Personal/ongoing/ttc_app/data.txt","r")
for line in file1:
    print(line.strip())
file1.close()