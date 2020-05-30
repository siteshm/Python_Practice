#program to calcute cosx - sinx = 0 or cosx = sinx 
#use google for plot graph reference , Search cosx-sinx=0 ,you'll get plot graph
import math # math module to compute cos and sin funtion

def f(x):
    return  math.cos(x) - math.sin(x)

x_l = 0 #lower boundary
x_u = 1 #upper boundary
x = (x_l + x_u)/2 # mid value
print(x)

while (abs(f(x)) > 0.001): #loop to check nearest value to 0 ex --0.001,0.0001
    print(x_l,x_u,x)
    
    #check value is greater than midpoint . change lower and upper boundary accordingly.
    x = (x_l + x_u)/2 
    if f(x) > 0:
        x_l = x
    else:
        x_u = x
    print(f(x),x_l,x_u)
print("x:" + str(x) + "\t f(x): " + str(f(x)))
    
        
        
    
    
    
    
    