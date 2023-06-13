# import modules

import cmath


# constants

PI = 3.1415926535897932384626433832795028841971693993751058209749445923


# help

def Explain():
    text = "This is a self defined sinus function ; input is the angle a or complex number a+b*j; output is sinus of angle a or complex number a+b*j."
    return text



# questions

def Questions(): 
    q = ['Enter a number: ']
    return q



# function

def Execute(x):
    y = x - x**3/6 + x**5/120 - x**7/5040 + x**9/362880 - x**11/39916800 + x**13/6227020800 - x**15/1307674368000 + x**17/355687428096000 - x**19/121645100408832000
    return y
