# import modules

import cmath


# constants

PI = 3.1415926535897932384626433832795028841971693993751058209749445923



# help

def Explain():
    text = "This is a self defined tangent function ; input is the angle a or complex number a+b*j; output is the tangent of angle a or complex number a+b*j."
    return text



# questions

def Questions(): 
    q = ['Enter a number: ']
    return q



# function

def Execute(x):
    y = x + x**3/3 + (2*x**5)/15 + (17*x**7)/315 + (62*x**9)/2835 + (1382*x**11)/155925 + (21844*x**13)/6081075 + (929569*x**15)/638512875 + (6404582*x**17)/10854718875 + (443861162*x**19)/1856156927625
    return y