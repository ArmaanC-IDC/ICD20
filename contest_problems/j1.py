g1 = input("W/L: ").lower()
g2 = input("W/L: ").lower()
g3 = input("W/L: ").lower()
g4 = input("W/L: ").lower()
g5 = input("W/L: ").lower()
g6 = input("please enter win or lose: ").lower()
list = [g1, g2, g3, g4, g5, g6]
w=0
for element in list:
    if element=='w':
        w+=1
if w==0:
    print('-1')
elif w==1 or w==2:
    print('3')
elif w==3 or w==4:
    print('2')
elif w==5 or w==6:
    print('1')