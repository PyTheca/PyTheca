# import modules

import cmath


# constants

PI = 3.1415926535897932384626433832795028841971693993751058209749445923




# help

def Explain():
    text = "This is a self defined cosinus function ; input is the angle a or complex number a+b*j; output is cosinus of angle a or complex number a+b*j."
    return text




# questions

def Questions(): 
    q = ['Enter a number: ']
    return q




# function

def Execute(x):
    y = 1 - x**2/2 + x**4/24 - x**6/720 + x**8/40320 - x**10/3628800 + x**12/479001600 - x**14/87178291200 + x**16/20922789888000 - x**18/6402373705728000
    return y
