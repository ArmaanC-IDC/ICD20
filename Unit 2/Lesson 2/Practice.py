'''x = input("string: ")
b = x[0:3]
print(b)'''



import math
def triangle_prism(a,b,c,h):
    return 1/4*h*math.sqrt((-1*a)**4*(a*b)*2+2*(a*c)*2-b**4+2*(b*c)*2-c**4)

a=1
b=2
c=3
h=4
print(f"{triangle_prism(a,b,c,h)}")