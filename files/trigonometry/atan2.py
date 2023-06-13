# import modules

import math


# constants

PI = 3.1415926535897932384626433832795028841971693993751058209749445923



# help

def Explain():
    text = "This is a self defined atan2 function ; input are the coordinates x and y; output is the corresponding angle in radians on a complete circle."
    return text




# questions

def Questions(): 
    q = ['Enter x coordinate: ', 'Enter y coordinate: ']
    return q



# function

def Execute(x,y):

    if x==0 and y==0:
        return ("Input Error")

    if x > 0 and y == 0:
        return (math.atan(y/x))
    
    if x > 0 and y > 0:
        return (math.atan(y/x))
    
    if x == 0 and y > 0:
        return (0.5 * PI)
    
    if x < 0 and y > 0:
        return (math.atan(y/x) + PI)
    
    if x < 0 and y == 0:
        return (PI)
    
    if x < 0 and y < 0:
        return (math.atan(y/x) - PI)
    
    if x == 0 and y < 0:
        return (-0.5 * PI)

    if x > 0 and y < 0:
        return (math.atan(y/x))



# copyright

def copyright():
    text = "Roelof Gerard Smit - 20220314"
    return text