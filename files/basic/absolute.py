# import modules

import cmath



# help

def Explain():
    text = "Input is the number a ; output is the absolute value of a."
    return text



# questions

def Questions(): 
    q = ['Enter a number: ']
    return q



# function

def Execute(x):
    if x < 0:
        x *= -1
        return x
    else:
        return x