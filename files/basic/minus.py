# import modules

import cmath



# help

def Explain():
    text = "Input are the numbers a , b or complex numbers a+b*j , c+d*j ; output is a-b or (a+b*j)-(c+d*j)."
    return text

# questions

def Questions(): 
    q = ['Enter 1st number: ', 'Enter 2nd number: ']
    return q


# function

def Execute(x,y):
    z = x - y
    return z